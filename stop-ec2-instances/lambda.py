import boto3

#define the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    #get all running instances
    all_running_instances = [i for i in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])]
    # get instances with filter of running + with tag `Name`
    instances = [i for i in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}, {'Name':'tag:AutoOff', 'Values':['true']}])]
    # make a list of filtered instances IDs `[i.id for i in instances]`
    
    instances_to_stop = [to_stop for to_stop in all_running_instances if to_stop.id in [i.id for i in instances]]
    if len(instances_to_stop) > 0:
        # run over your `instances_to_stop` list and terminate each one of them
        for instance in instances_to_stop:
            shuttingDown = instance.stop()
            print(shuttingDown)