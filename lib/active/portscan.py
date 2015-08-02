
try:
	import datetime
	from lib.core.config_parser import ConfigParser
	from lib.active.corescanner import CoreScanner
except ImportError, err:
	from lib.core.core import Core
	Core.print_error(err)


class PortScan(CoreScanner):

    	def __init__(self, config_file, output_dir, ip_file_to_scan, nmap_optimize, scan_type):

		self.ip_file_to_scan = ip_file_to_scan
		self.scan_options = ConfigParser.get_ports_options(config_file)

		output_file = "{0}{1}-{2}".format(output_dir, scan_type, datetime.datetime.now().strftime("%Y%m%d%H%M"))
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
        	CoreScanner.__init__(self, self.ip_file_to_scan.name, output_file, nmap_optimize, scan_type)


