
# ============================================================
# Python Tuples
# File: 05_tuples.py
# ============================================================

# 1. Creating tuples

cloud_providers = ("AWS", "Azure", "GCP")
ports = (80, 443, 8080)
server_details = ("web-01", "192.168.1.10", "running", 8080)

print("Cloud providers:", cloud_providers)
print("Ports:", ports)
print("Server details:", server_details)

# 2. Creating a single-element tuple

single_provider = ("AWS",)

print("\nSingle-element tuple:", single_provider)
print("Type:", type(single_provider))

# 3. Accessing tuple elements

print("\nFirst provider:", cloud_providers[0])
print("Last provider:", cloud_providers[-1])

# 4. Tuple slicing

tools = ("Docker", "Kubernetes", "Terraform", "Ansible", "Jenkins")

print("\nFirst three tools:", tools[:3])
print("Last two tools:", tools[-2:])
print("Reversed tools:", tools[::-1])

# 5. Checking tuple length

print("\nNumber of tools:", len(tools))

# 6. Checking whether an element exists

print("Docker available:", "Docker" in tools)
print("Python available:", "Python" in tools)

# 7. Tuple methods

numbers = (10, 20, 30, 20, 40, 20)

print("\nCount of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

# 8. Looping through a tuple

print("\nAvailable tools:")

for tool in tools:
    print(tool)

# 9. Looping with index

print("\nTools with indexes:")

for index, tool in enumerate(tools):
    print(f"{index}: {tool}")

# 10. Tuple unpacking

server = ("web-01", "192.168.1.10", "running")

server_name, server_ip, server_status = server

print("\nServer information:")
print("Name:", server_name)
print("IP:", server_ip)
print("Status:", server_status)

# 11. Extended unpacking

technologies = ("Python", "Java", "Docker", "Kubernetes")

first_technology, *remaining_technologies = technologies

print("\nFirst technology:", first_technology)
print("Remaining technologies:", remaining_technologies)

# 12. Combining tuples

frontend = ("React", "Angular")
backend = ("Python", "Java")

full_stack = frontend + backend

print("\nFull-stack technologies:", full_stack)

# 13. Adding an element by creating a new tuple

cloud_providers = cloud_providers + ("Oracle",)

print("\nUpdated cloud providers:", cloud_providers)

# 14. Removing an element by creating a new tuple

tools = ("Docker", "Kubernetes", "Terraform", "Ansible")

updated_tools = tools[:1] + tools[2:]

print("\nUpdated tools:", updated_tools)

# 15. Converting a tuple into a list and back

environments = ("dev", "test", "staging")

environment_list = list(environments)
environment_list.append("production")

environments = tuple(environment_list)

print("\nUpdated environments:", environments)

# 16. Nested tuples

servers = (
    ("web-01", "192.168.1.10", "running"),
    ("web-02", "192.168.1.11", "stopped"),
    ("db-01", "192.168.1.20", "running")
)

print("\nServer inventory:")

for name, ip_address, status in servers:
    print(f"{name} | {ip_address} | {status}")

# 17. Useful built-in functions

resource_usage = (25, 40, 60, 80, 35)

print("\nMinimum usage:", min(resource_usage))
print("Maximum usage:", max(resource_usage))
print("Total usage:", sum(resource_usage))
print("Number of records:", len(resource_usage))

# 18. Nested mutable object

server_config = ("web-01", ["Docker", "Nginx"])

server_config[1].append("Prometheus")

print("\nUpdated server configuration:", server_config)
