import geni.portal as portal
import geni.rspec.pg as pg

# Create a portal context and define parameters
pc = portal.Context()
pc.defineParameter("nodeCount", "Number of Nodes", portal.ParameterType.INTEGER, 1)
params = pc.bindParameters()

# Create a Request object
request = pc.makeRequestRSpec()

# Create nodes and set disk image
for i in range(params.nodeCount):
    node = request.RawPC("node" + str(i))
    node.disk_image = "urn:publicid:IDN+wisc.cloudlab.us+image+distribml-PG0:python-setup.node0-nvidia-cuda"
    node.addService(pg.Execute(shell="sh", command="/local/repository/setup.sh"))

# Output the request RSpec
pc.printRequestRSpec(request)
