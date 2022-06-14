import subprocess

try:
  subprocess.run(["ping", "www.marcombo.com","-n","5"])
  #en linux
  #subprocess.run(["ping", "www.marcombo.com","-c","5"])
except subprocess.CalledProcessError as e:
    print(e.output)