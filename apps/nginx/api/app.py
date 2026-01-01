from flask import Flask, jsonify
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/stats')
def stats():
    with open('/proc/meminfo') as f:
        for line in f:
            if line.startswith('MemTotal:'):
                total_ram = int(line.split()[1]) / 1024
                break

    containers = []
    total_used = 0

    for c in client.containers.list():
        s = c.stats(stream=False)
        mem_usage = s['memory_stats'].get('usage', 0) / 1024 / 1024
        mem_limit = s['memory_stats'].get('limit', 0) / 1024 / 1024

        ports = []
        for container_port, host_bindings in (c.attrs['NetworkSettings']['Ports'] or {}).items():
            if host_bindings:
                for binding in host_bindings:
                    if binding['HostPort'] not in ports:
                        ports.append(binding['HostPort'])

        containers.append({
            'name': c.name,
            'used': round(mem_usage, 2),
            'limit': round(mem_limit, 2),
            'unused': round(mem_limit - mem_usage, 2) if mem_limit > mem_usage else 0,
            'ports': ports
        })
        total_used += mem_usage

    return jsonify({
        'total_ram': round(total_ram, 2),
        'free_ram': round(total_ram - total_used, 2),
        'containers': containers
    })

@app.after_request
def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
