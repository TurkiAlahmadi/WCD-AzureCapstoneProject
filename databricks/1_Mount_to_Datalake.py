# Databricks notebook source
StrgAccName = "cp2dl"
ContnrName = "bd-project"
MntPoint = "/mnt/bd-project"
ScrtKey = dbutils.secrets.get(scope="cp2kvscope", key="StrgAccAccessKey") # Add secret scope to integrate Azure KeyValut

if not any(mount.mountPoint == MntPoint for mount in dbutils.fs.mounts()):
  try:
    dbutils.fs.mount(
      source = "wasbs://{ContnrName}@{StrgAccName}.blob.core.windows.net".format(ContnrName=ContnrName, StrgAccName=StrgAccName),
      mount_point = MntPoint,
      extra_configs = {"fs.azure.account.key.{StrgAccName}.blob.core.windows.net".format(StrgAccName=StrgAccName): ScrtKey}
    )
    print("mount succeeded!")
  except Exception as e:
    print("mount exception:", e)
