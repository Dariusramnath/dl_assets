import subprocess

def dwnld_img(url, filename):

  # Create the curl command
  command = ["curl", "-L", "-o", filename, url]
  
  # Run the command using subprocess
  subprocess.run(command)