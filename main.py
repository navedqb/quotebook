from datetime import datetime
import pkg_resources

now = datetime.now()
version = pkg_resources.get_distribution("virtualenv").version

print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("VirtualEnv version:", version)
