import geni.portal as portal
import geni.rspec.pg as pg

# Create a portal context and define parameters
pc = portal.Context()
pc.defineParameter("nodeCount", "Number of Nodes", portal.ParameterType.INTEGER, 1)
pc.defineParameter("phystype",  "Optional physical node type",
                   portal.ParameterType.NODETYPE, "",
                   longDescription="Pick a single physical node type (pc3000,d710,etc) " +
                   "instead of letting the resource mapper choose for you.")
params = pc.bindParameters()

# Create a Request object
request = pc.makeRequestRSpec()

# Create nodes and set disk image
for i in range(params.nodeCount):
    node = request.RawPC("node" + str(i))
    node.disk_image = "urn:publicid:IDN+wisc.cloudlab.us+image+distribml-PG0:python-setup.node0-nvidia-cuda"
    # node.addService(pg.Execute(shell="sh", command="/local/repository/setup.sh"))

# Output the request RSpec
pc.printRequestRSpec(request)
