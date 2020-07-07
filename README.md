# Nest
Custom helper class to concatenate arbitrarily nested jsonObjects/jsonStrings/list/dictionary objects into one key value set.
* Compatible with Python 2.7.x
* Compatible with Python 3.6.x

Practicality: Extract the instanceId thats nested deeply within a AWS RunInstances nested python dictionary

You could do it the old way
* instanceId = json.loads(RunInstances['Records'][0]['Sns']['Message'])['detail']['responseElements']['instancesSet']['items'][0]['instanceId']

Or the new way with Nest
* instanceId = Nest(RunInstances).instanceId
* instanceId = Nest(RunInstances)['instanceId']


## What is a nested object?
Let there be two objects, ojectA and objectB.
* If objectA is contained within objectB then objectA is 'nested' within objectB.
* If objectB contains objectA, objectB is a 'nest' of objects.

## Contents
* [Installation](#installation)
* [Acceptable Input](#acceptable_input)
* [Functionality](#functionality)
* [Examples](#examples)

## Installation
```javascript
1) Download this repo, then extract the contents.

2) Within the extracted contents there is a 'Nest' folder, copy the 'Nest' folder

3) Use python from your terminal to reveal the site-packages directory you can choose from
   Example:
   >python
   >>>import sys
   >>>print(' '.join(sys.path))
        C:\Users\LANIERK\AppData\Roaming\Python\Python27\site-packages C:\Python27\lib\site-packages


4) Copy your downloaded 'Nest' module folder to one of the'site-packages' directories that sys provided you

5) From within your python scripts, import the new module as:
   Example: from Nest.Nest import Nest

6) Now you can use the Nest module
   Example: myNest = Nest(<someNestedObject>)
```

## Acceptable_input
```javascript
Definitions:
* Let J  = <yourJsonObject> 
* Let L  = [<yourListItems>]
* Let D  = {<yourKeyValuePairs>}
* Let N  = <list | dictionary | json> that contains at least one <list | dictionary | json>
* Let Nn = <list | dictionary | json> that contains any number, level, or combination of <list | dictionary | json>
* Let N+ = <Nest(J) | Nest(D) | Nest(N) | Nest(Nn)> that contains any number, level, or combination of <Nest(J) | Nest(D) | Nest(N) | Nest(Nn)>


Examples:
* myNest = Nest(J)
* myNest = Nest(D)
* myNest = Nest(N)
* myNest = Nest(Nn)
* myNest = Nest(N+)
```

## Functionality
```javascript
Nest() will recurse through items contained within the received nest. 
Starting with the first level of the nest, L1, if another level is detected, L2, 
then the <dictionaryKeys | listIndexes> of L2 will be appended to '_' which are 
then appended to the <dictionaryKeys | listIndexes> of L1.


## Standard Functions
* myNest.items()  # will return a flatened dictionary of key value pairs, ie {k,v}
* myNest.keys()   # will return a list of keys, ie [key1, key2, ... ]
* myNest.values() # will return a list of values, ie [value1, value2, ... ]

## Special Functions
The '.' operator, __getattr__, allows the use of 'subkeys'
The [' '] operator, __getitem__, allows the use of 'subkeys'

* If a subkey is found within multiple keys, a dictionary of the found key value pairs is returned
* If a subkey is found within only one key, the value of the key is returned
* If a subkey is not found, None is returned
```

## EXAMPLES
```javascript
This is a standard cloudwatch RunInstances event that contains multiple nested objects.

# defining mappings from json values to a python object for local testing
null = None
true = True
false = False

RunInstances = {
    "Records": [
        {
            "EventSource": "aws:sns",
            "EventVersion": "1.0",
            "EventSubscriptionArn": "arn:aws:sns:us-east-1:546754328912:aws-ec2-runinstances:5e378273-4e5d-422f-8058-c9a94703e39c",
            "Sns": {
                "Type": "Notification",
                "MessageId": "816d7f5c-c290-5dbe-85fe-2db22b0d4308",
                "TopicArn": "arn:aws:sns:us-east-1:546754328912:aws-ec2-runinstances",
                "Subject": null,
                "Message": "{\"version\":\"0\",\"id\":\"c4b25530-80f2-5d79-7de1-806bc32c8b3d\",\"detail-type\":\"AWS API Call via CloudTrail\",\"source\":\"aws.ec2\",\"account\":\"546754328912\",\"time\":\"2018-02-02T22:33:05Z\",\"region\":\"us-east-1\",\"resources\":[],\"detail\":{\"eventVersion\":\"1.05\",\"userIdentity\":{\"type\":\"AssumedRole\",\"principalId\":\"AROAIBPZGA5H2JMAKH3DM:LANIERK\",\"arn\":\"arn:aws:sts::546754328912:assumed-role/platform--platform/LANIERK\",\"accountId\":\"546754328912\",\"accessKeyId\":\"ASIAJFA7WV5DZ745WQDQ\",\"sessionContext\":{\"attributes\":{\"mfaAuthenticated\":\"false\",\"creationDate\":\"2018-02-02T22:26:51Z\"},\"sessionIssuer\":{\"type\":\"Role\",\"principalId\":\"AROAIBPZGA5H2JMAKH3DM\",\"arn\":\"arn:aws:iam::546754328912:role/-platform\",\"accountId\":\"546754328912\",\"userName\":\"-platform\"}}},\"eventTime\":\"2018-02-02T22:33:05Z\",\"eventSource\":\"ec2.amazonaws.com\",\"eventName\":\"RunInstances\",\"awsRegion\":\"us-east-1\",\"sourceIPAddress\":\"165.225.34.106\",\"userAgent\":\"console.ec2.amazonaws.com\",\"requestParameters\":{\"instancesSet\":{\"items\":[{\"imageId\":\"ami-603b1c1a\",\"minCount\":1,\"maxCount\":1,\"keyName\":\"KyleLanierTest\"}]},\"instanceType\":\"t2.micro\",\"blockDeviceMapping\":{\"items\":[{\"deviceName\":\"/dev/sda1\",\"ebs\":{\"volumeSize\":30,\"deleteOnTermination\":true,\"volumeType\":\"gp2\"}},{\"deviceName\":\"xvdca\",\"noDevice\":{}},{\"deviceName\":\"xvdcb\",\"noDevice\":{}},{\"deviceName\":\"xvdcc\",\"noDevice\":{}},{\"deviceName\":\"xvdcd\",\"noDevice\":{}},{\"deviceName\":\"xvdce\",\"noDevice\":{}},{\"deviceName\":\"xvdcf\",\"noDevice\":{}},{\"deviceName\":\"xvdcg\",\"noDevice\":{}},{\"deviceName\":\"xvdch\",\"noDevice\":{}},{\"deviceName\":\"xvdci\",\"noDevice\":{}},{\"deviceName\":\"xvdcj\",\"noDevice\":{}},{\"deviceName\":\"xvdck\",\"noDevice\":{}},{\"deviceName\":\"xvdcl\",\"noDevice\":{}},{\"deviceName\":\"xvdcm\",\"noDevice\":{}},{\"deviceName\":\"xvdcn\",\"noDevice\":{}},{\"deviceName\":\"xvdco\",\"noDevice\":{}},{\"deviceName\":\"xvdcp\",\"noDevice\":{}},{\"deviceName\":\"xvdcq\",\"noDevice\":{}},{\"deviceName\":\"xvdcr\",\"noDevice\":{}},{\"deviceName\":\"xvdcs\",\"noDevice\":{}},{\"deviceName\":\"xvdct\",\"noDevice\":{}},{\"deviceName\":\"xvdcu\",\"noDevice\":{}},{\"deviceName\":\"xvdcv\",\"noDevice\":{}},{\"deviceName\":\"xvdcw\",\"noDevice\":{}},{\"deviceName\":\"xvdcx\",\"noDevice\":{}},{\"deviceName\":\"xvdcy\",\"noDevice\":{}},{\"deviceName\":\"xvdcz\",\"noDevice\":{}}]},\"tenancy\":\"default\",\"monitoring\":{\"enabled\":false},\"disableApiTermination\":false,\"instanceInitiatedShutdownBehavior\":\"stop\",\"networkInterfaceSet\":{\"items\":[{\"deviceIndex\":0,\"subnetId\":\"subnet-96294bbb\",\"description\":\"Primary network interface\",\"deleteOnTermination\":true,\"groupSet\":{\"items\":[{\"groupId\":\"sg-e6fc1d9a\"}]},\"ipv6AddressCount\":0}]},\"ebsOptimized\":false,\"tagSpecificationSet\":{\"items\":[{\"resourceType\":\"instance\",\"tags\":[{\"key\":\"BLC\",\"value\":\"1539\"},{\"key\":\"CostCenter\",\"value\":\"54111\"},{\"key\":\"Name\",\"value\":\"KyleLanierTagTesting\"},{\"key\":\"Owner\",\"value\":\"cloudengineering@testing.com\"}]},{\"resourceType\":\"volume\",\"tags\":[{\"key\":\"BLC\",\"value\":\"1539\"},{\"key\":\"CostCenter\",\"value\":\"54111\"},{\"key\":\"Name\",\"value\":\"KyleLanierTagTesting\"},{\"key\":\"Owner\",\"value\":\"cloudengineering@testing.com\"}]}]},\"creditSpecification\":{\"cpuCredits\":\"standard\"}},\"responseElements\":{\"requestId\":\"ef3e38cb-7772-4840-9fc6-f345d8767a24\",\"reservationId\":\"r-0cee6e22ba20abc4b\",\"ownerId\":\"546754328912\",\"groupSet\":{},\"instancesSet\":{\"items\":[{\"instanceId\":\"i-0a626ccee68ff585c\",\"imageId\":\"ami-603b1c1a\",\"instanceState\":{\"code\":0,\"name\":\"pending\"},\"privateDnsName\":\"ip-10-225-249-73.ec2.internal\",\"keyName\":\"KyleLanierTest\",\"amiLaunchIndex\":0,\"productCodes\":{},\"instanceType\":\"t2.micro\",\"launchTime\":1517610785000,\"placement\":{\"availabilityZone\":\"us-east-1b\",\"tenancy\":\"default\"},\"platform\":\"windows\",\"monitoring\":{\"state\":\"disabled\"},\"subnetId\":\"subnet-96294bbb\",\"vpcId\":\"vpc-102e8276\",\"privateIpAddress\":\"10.225.249.73\",\"stateReason\":{\"code\":\"pending\",\"message\":\"pending\"},\"architecture\":\"x86_64\",\"rootDeviceType\":\"ebs\",\"rootDeviceName\":\"/dev/sda1\",\"blockDeviceMapping\":{},\"virtualizationType\":\"hvm\",\"hypervisor\":\"xen\",\"tagSet\":{\"items\":[{\"key\":\"BLC\",\"value\":\"1539\"},{\"key\":\"CostCenter\",\"value\":\"54111\"},{\"key\":\"Name\",\"value\":\"KyleLanierTagTesting\"},{\"key\":\"Owner\",\"value\":\"cloudengineering@testing.com\"}]},\"groupSet\":{\"items\":[{\"groupId\":\"sg-e6fc1d9a\",\"groupName\":\"Allow All\"}]},\"sourceDestCheck\":true,\"networkInterfaceSet\":{\"items\":[{\"networkInterfaceId\":\"eni-2a62d5e7\",\"subnetId\":\"subnet-96294bbb\",\"vpcId\":\"vpc-102e8276\",\"description\":\"Primary network interface\",\"ownerId\":\"546754328912\",\"status\":\"in-use\",\"macAddress\":\"12:1e:c2:a1:b7:a8\",\"privateIpAddress\":\"10.225.249.73\",\"privateDnsName\":\"ip-10-225-249-73.ec2.internal\",\"sourceDestCheck\":true,\"groupSet\":{\"items\":[{\"groupId\":\"sg-e6fc1d9a\",\"groupName\":\"Allow All\"}]},\"attachment\":{\"attachmentId\":\"eni-attach-cfe88002\",\"deviceIndex\":0,\"status\":\"attaching\",\"attachTime\":1517610785000,\"deleteOnTermination\":true},\"privateIpAddressesSet\":{\"item\":[{\"privateIpAddress\":\"10.225.249.73\",\"privateDnsName\":\"ip-10-225-249-73.ec2.internal\",\"primary\":true}]},\"ipv6AddressesSet\":{},\"tagSet\":{}}]},\"ebsOptimized\":false}]}},\"requestID\":\"ef3e38cb-7772-4840-9fc6-f345d8767a24\",\"eventID\":\"20874fa9-d1ae-4e91-bec3-382bb426360a\",\"eventType\":\"AwsApiCall\"}}",
                "Timestamp": "2018-02-02T22:34:05.710Z",
                "SignatureVersion": "1",
                "Signature": "MOSzUgv7AgohTgIOBLzGromPN3gEmeYJbpEfXOZNLsrDVuoBfNFmy08q+QMti2fdoqasgHRqPljrXFD4lg0KPcsSnuPOyyGaB4lzVWb79i45fjm0bTtWq+ANQdt/sMqHxqnoBF/o5q130rhMEqcm6x3h4/PCv/KhcWbtSXdU2CAfa5nvul2NHv2zZx6GzWcLrBniyvGBt1muSdIEupBshE+zv0q9pbVIfWymtHigYEvdvYO7xsdm5UDTsEwn86ui4XYTOOaZUgoNNfJuX0GmiVdGtZwtCnjrJkmhFPcrAOwqHk+wYzhhfGnKTmqLeMcYZ0njhuO9zjVErSvcbPVVew==",
                "SigningCertUrl": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-433026a4050d206028891664da859041.pem",
                "UnsubscribeUrl": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:546754328912:aws-ec2-runinstances:5e378273-4e5d-422f-8058-c9a94703e39c",
                "MessageAttributes": {
                    "accountId": {
                        "Type": "String",
                        "Value": "546754328912"
                    },
                    "eventName": {
                        "Type": "String",
                        "Value": "RunInstances"
                    }
                }
            }
        }
    ]
}

Lets de-nest our RunInstances event

myNest = Nest(RunInstances)

# myNest.items()
Will return: {
    'Records_0_EventSource': 'aws:sns',
    'Records_0_EventSubscriptionArn': 'arn:aws:sns:us-east-1:546754328912:aws-ec2-runinstances:5e378273-4e5d-422f-8058-c9a94703e39c',
    'Records_0_EventVersion': 1.0,
    'Records_0_Sns_MessageAttributes_accountId_Type': 'String',
    'Records_0_Sns_MessageAttributes_accountId_Value': 546754328912,
    'Records_0_Sns_MessageAttributes_eventName_Type': 'String',
    'Records_0_Sns_MessageAttributes_eventName_Value': 'RunInstances',
    'Records_0_Sns_MessageId': '816d7f5c-c290-5dbe-85fe-2db22b0d4308',
    'Records_0_Sns_Message_account': 546754328912,
    'Records_0_Sns_Message_detail-type': 'AWS API Call via CloudTrail',
    'Records_0_Sns_Message_detail_awsRegion': 'us-east-1',
    'Records_0_Sns_Message_detail_eventID': '20874fa9-d1ae-4e91-bec3-382bb426360a',
    'Records_0_Sns_Message_detail_eventName': 'RunInstances',
    'Records_0_Sns_Message_detail_eventSource': 'ec2.amazonaws.com',
    'Records_0_Sns_Message_detail_eventTime': '2018-02-02T22:33:05Z',
    'Records_0_Sns_Message_detail_eventType': 'AwsApiCall',
    'Records_0_Sns_Message_detail_eventVersion': 1.05,
    'Records_0_Sns_Message_detail_requestID': 'ef3e38cb-7772-4840-9fc6-f345d8767a24',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_0_deviceName': '/dev/sda1',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_0_ebs_deleteOnTermination': True,
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_0_ebs_volumeSize': 30,
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_0_ebs_volumeType': 'gp2',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_10_deviceName': 'xvdcj',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_11_deviceName': 'xvdck',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_12_deviceName': 'xvdcl',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_13_deviceName': 'xvdcm',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_14_deviceName': 'xvdcn',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_15_deviceName': 'xvdco',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_16_deviceName': 'xvdcp',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_17_deviceName': 'xvdcq',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_18_deviceName': 'xvdcr',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_19_deviceName': 'xvdcs',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_1_deviceName': 'xvdca',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_20_deviceName': 'xvdct',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_21_deviceName': 'xvdcu',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_22_deviceName': 'xvdcv',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_23_deviceName': 'xvdcw',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_24_deviceName': 'xvdcx',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_25_deviceName': 'xvdcy',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_26_deviceName': 'xvdcz',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_2_deviceName': 'xvdcb',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_3_deviceName': 'xvdcc',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_4_deviceName': 'xvdcd',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_5_deviceName': 'xvdce',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_6_deviceName': 'xvdcf',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_7_deviceName': 'xvdcg',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_8_deviceName': 'xvdch',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_9_deviceName': 'xvdci',
    'Records_0_Sns_Message_detail_requestParameters_creditSpecification_cpuCredits': 'standard',
    'Records_0_Sns_Message_detail_requestParameters_disableApiTermination': False,
    'Records_0_Sns_Message_detail_requestParameters_ebsOptimized': False,
    'Records_0_Sns_Message_detail_requestParameters_instanceInitiatedShutdownBehavior': 'stop',
    'Records_0_Sns_Message_detail_requestParameters_instanceType': 't2.micro',
    'Records_0_Sns_Message_detail_requestParameters_instancesSet_items_0_imageId': 'ami-603b1c1a',
    'Records_0_Sns_Message_detail_requestParameters_instancesSet_items_0_keyName': 'KyleLanierTest',
    'Records_0_Sns_Message_detail_requestParameters_instancesSet_items_0_maxCount': 1,
    'Records_0_Sns_Message_detail_requestParameters_instancesSet_items_0_minCount': 1,
    'Records_0_Sns_Message_detail_requestParameters_monitoring_enabled': False,
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_deleteOnTermination': True,
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_description': 'Primary network interface',
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_deviceIndex': 0,
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_groupSet_items_0_groupId': 'sg-e6fc1d9a',
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_ipv6AddressCount': 0,
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_subnetId': 'subnet-96294bbb',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_resourceType': 'instance',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_0_key': 'BLC',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_0_value': 1539,
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_1_key': 'CostCenter',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_1_value': 54111,
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_2_key': 'Name',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_2_value': 'KyleLanierTagTesting',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_3_key': 'Owner',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_3_value': 'cloudengineering@testing.com',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_resourceType': 'volume',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_0_key': 'BLC',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_0_value': 1539,
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_1_key': 'CostCenter',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_1_value': 54111,
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_2_key': 'Name',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_2_value': 'KyleLanierTagTesting',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_3_key': 'Owner',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_3_value': 'cloudengineering@testing.com',
    'Records_0_Sns_Message_detail_requestParameters_tenancy': 'default',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_amiLaunchIndex': 0,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_architecture': 'x86_64',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_ebsOptimized': False,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_groupSet_items_0_groupId': 'sg-e6fc1d9a',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_groupSet_items_0_groupName': 'Allow All',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_hypervisor': 'xen',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_imageId': 'ami-603b1c1a',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_instanceId': 'i-0a626ccee68ff585c',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_instanceState_code': 0,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_instanceState_name': 'pending',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_instanceType': 't2.micro',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_keyName': 'KyleLanierTest',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_launchTime': 1517610785000,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_monitoring_state': 'disabled',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_attachment_attachTime': 1517610785000,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_attachment_attachmentId': 'eni-attach-cfe88002',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_attachment_deleteOnTermination': True,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_attachment_deviceIndex': 0,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_attachment_status': 'attaching',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_description': 'Primary network interface',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_groupSet_items_0_groupId': 'sg-e6fc1d9a',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_groupSet_items_0_groupName': 'Allow All',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_macAddress': '12:1e:c2:a1:b7:a8',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_networkInterfaceId': 'eni-2a62d5e7',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_ownerId': 546754328912,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateDnsName': 'ip-10-225-249-73.ec2.internal',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddress': '10.225.249.73',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_primary': True,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_privateDnsName': 'ip-10-225-249-73.ec2.internal',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_privateIpAddress': '10.225.249.73',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_sourceDestCheck': True,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_status': 'in-use',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_subnetId': 'subnet-96294bbb',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_vpcId': 'vpc-102e8276',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_placement_availabilityZone': 'us-east-1b',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_placement_tenancy': 'default',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_platform': 'windows',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_privateDnsName': 'ip-10-225-249-73.ec2.internal',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_privateIpAddress': '10.225.249.73',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_rootDeviceName': '/dev/sda1',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_rootDeviceType': 'ebs',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_sourceDestCheck': True,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_stateReason_code': 'pending',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_stateReason_message': 'pending',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_subnetId': 'subnet-96294bbb',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_0_key': 'BLC',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_0_value': 1539,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_1_key': 'CostCenter',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_1_value': 54111,
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_2_key': 'Name',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_2_value': 'KyleLanierTagTesting',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_3_key': 'Owner',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_3_value': 'cloudengineering@testing.com',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_virtualizationType': 'hvm',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_vpcId': 'vpc-102e8276',
    'Records_0_Sns_Message_detail_responseElements_ownerId': 546754328912,
    'Records_0_Sns_Message_detail_responseElements_requestId': 'ef3e38cb-7772-4840-9fc6-f345d8767a24',
    'Records_0_Sns_Message_detail_responseElements_reservationId': 'r-0cee6e22ba20abc4b',
    'Records_0_Sns_Message_detail_sourceIPAddress': '165.225.34.106',
    'Records_0_Sns_Message_detail_userAgent': 'console.ec2.amazonaws.com',
    'Records_0_Sns_Message_detail_userIdentity_accessKeyId': 'ASIAJFA7WV5DZ745WQDQ',
    'Records_0_Sns_Message_detail_userIdentity_accountId': 546754328912,
    'Records_0_Sns_Message_detail_userIdentity_arn': 'arn:aws:sts::546754328912:assumed-role/platform--platform/LANIERK',
    'Records_0_Sns_Message_detail_userIdentity_principalId': 'AROAIBPZGA5H2JMAKH3DM:LANIERK',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_attributes_creationDate': '2018-02-02T22:26:51Z',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_attributes_mfaAuthenticated': False,
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_sessionIssuer_accountId': 546754328912,
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_sessionIssuer_arn': 'arn:aws:iam::546754328912:role/-platform',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_sessionIssuer_principalId': 'AROAIBPZGA5H2JMAKH3DM',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_sessionIssuer_type': 'Role',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_sessionIssuer_userName': '-platform',
    'Records_0_Sns_Message_detail_userIdentity_type': 'AssumedRole',
    'Records_0_Sns_Message_id': 'c4b25530-80f2-5d79-7de1-806bc32c8b3d',
    'Records_0_Sns_Message_region': 'us-east-1',
    'Records_0_Sns_Message_source': 'aws.ec2',
    'Records_0_Sns_Message_time': '2018-02-02T22:33:05Z',
    'Records_0_Sns_Message_version': 0,
    'Records_0_Sns_Signature': 'MOSzUgv7AgohTgIOBLzGromPN3gEmeYJbpEfXOZNLsrDVuoBfNFmy08q+QMti2fdoqasgHRqPljrXFD4lg0KPcsSnuPOyyGaB4lzVWb79i45fjm0bTtWq+ANQdt/sMqHxqnoBF/o5q130rhMEqcm6x3h4/PCv/KhcWbtSXdU2CAfa5nvul2NHv2zZx6GzWcLrBniyvGBt1muSdIEupBshE+zv0q9pbVIfWymtHigYEvdvYO7xsdm5UDTsEwn86ui4XYTOOaZUgoNNfJuX0GmiVdGtZwtCnjrJkmhFPcrAOwqHk+wYzhhfGnKTmqLeMcYZ0njhuO9zjVErSvcbPVVew==',
    'Records_0_Sns_SignatureVersion': 1,
    'Records_0_Sns_SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-433026a4050d206028891664da859041.pem',
    'Records_0_Sns_Subject': None,
    'Records_0_Sns_Timestamp': '2018-02-02T22:34:05.710Z',
    'Records_0_Sns_TopicArn': 'arn:aws:sns:us-east-1:546754328912:aws-ec2-runinstances',
    'Records_0_Sns_Type': 'Notification',
    'Records_0_Sns_UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:546754328912:aws-ec2-runinstances:5e378273-4e5d-422f-8058-c9a94703e39c'
}

# myNest.keys()
Will return: [
    'Records_0_EventSource',
    'Records_0_EventVersion',
    'Records_0_EventSubscriptionArn',
    'Records_0_Sns_Type',
    'Records_0_Sns_MessageId',
    'Records_0_Sns_TopicArn',
    'Records_0_Sns_Subject',
    'Records_0_Sns_Message_version',
    'Records_0_Sns_Message_id',
    'Records_0_Sns_Message_detail-type',
    'Records_0_Sns_Message_source',
    'Records_0_Sns_Message_account',
    'Records_0_Sns_Message_time',
    'Records_0_Sns_Message_region',
    'Records_0_Sns_Message_detail_eventVersion',
    'Records_0_Sns_Message_detail_userIdentity_type',
    'Records_0_Sns_Message_detail_userIdentity_principalId',
    'Records_0_Sns_Message_detail_userIdentity_arn',
    'Records_0_Sns_Message_detail_userIdentity_accountId',
    'Records_0_Sns_Message_detail_userIdentity_accessKeyId',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_attributes_mfaAuthenticated',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_attributes_creationDate',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_sessionIssuer_type',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_sessionIssuer_principalId',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_sessionIssuer_arn',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_sessionIssuer_accountId',
    'Records_0_Sns_Message_detail_userIdentity_sessionContext_sessionIssuer_userName',
    'Records_0_Sns_Message_detail_eventTime',
    'Records_0_Sns_Message_detail_eventSource',
    'Records_0_Sns_Message_detail_eventName',
    'Records_0_Sns_Message_detail_awsRegion',
    'Records_0_Sns_Message_detail_sourceIPAddress',
    'Records_0_Sns_Message_detail_userAgent',
    'Records_0_Sns_Message_detail_requestParameters_instancesSet_items_0_imageId',
    'Records_0_Sns_Message_detail_requestParameters_instancesSet_items_0_minCount',
    'Records_0_Sns_Message_detail_requestParameters_instancesSet_items_0_maxCount',
    'Records_0_Sns_Message_detail_requestParameters_instancesSet_items_0_keyName',
    'Records_0_Sns_Message_detail_requestParameters_instanceType',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_0_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_0_ebs_volumeSize',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_0_ebs_deleteOnTermination',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_0_ebs_volumeType',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_1_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_2_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_3_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_4_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_5_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_6_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_7_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_8_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_9_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_10_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_11_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_12_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_13_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_14_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_15_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_16_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_17_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_18_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_19_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_20_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_21_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_22_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_23_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_24_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_25_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_blockDeviceMapping_items_26_deviceName',
    'Records_0_Sns_Message_detail_requestParameters_tenancy',
    'Records_0_Sns_Message_detail_requestParameters_monitoring_enabled',
    'Records_0_Sns_Message_detail_requestParameters_disableApiTermination',
    'Records_0_Sns_Message_detail_requestParameters_instanceInitiatedShutdownBehavior',
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_deviceIndex',
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_subnetId',
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_description',
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_deleteOnTermination',
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_groupSet_items_0_groupId',
    'Records_0_Sns_Message_detail_requestParameters_networkInterfaceSet_items_0_ipv6AddressCount',
    'Records_0_Sns_Message_detail_requestParameters_ebsOptimized',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_resourceType',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_0_key',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_0_value',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_1_key',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_1_value',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_2_key',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_2_value',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_3_key',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_0_tags_3_value',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_resourceType',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_0_key',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_0_value',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_1_key',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_1_value',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_2_key',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_2_value',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_3_key',
    'Records_0_Sns_Message_detail_requestParameters_tagSpecificationSet_items_1_tags_3_value',
    'Records_0_Sns_Message_detail_requestParameters_creditSpecification_cpuCredits',
    'Records_0_Sns_Message_detail_responseElements_requestId',
    'Records_0_Sns_Message_detail_responseElements_reservationId',
    'Records_0_Sns_Message_detail_responseElements_ownerId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_instanceId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_imageId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_instanceState_code',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_instanceState_name',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_privateDnsName',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_keyName',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_amiLaunchIndex',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_instanceType',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_launchTime',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_placement_availabilityZone',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_placement_tenancy',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_platform',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_monitoring_state',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_subnetId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_vpcId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_privateIpAddress',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_stateReason_code',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_stateReason_message',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_architecture',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_rootDeviceType',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_rootDeviceName',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_virtualizationType',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_hypervisor',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_0_key',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_0_value',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_1_key',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_1_value',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_2_key',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_2_value',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_3_key',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_tagSet_items_3_value',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_groupSet_items_0_groupId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_groupSet_items_0_groupName',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_sourceDestCheck',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_networkInterfaceId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_subnetId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_vpcId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_description',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_ownerId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_status',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_macAddress',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddress',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateDnsName',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_sourceDestCheck',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_groupSet_items_0_groupId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_groupSet_items_0_groupName',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_attachment_attachmentId',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_attachment_deviceIndex',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_attachment_status',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_attachment_attachTime',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_attachment_deleteOnTermination',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_privateIpAddress',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_privateDnsName',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_primary',
    'Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_ebsOptimized',
    'Records_0_Sns_Message_detail_requestID',
    'Records_0_Sns_Message_detail_eventID',
    'Records_0_Sns_Message_detail_eventType',
    'Records_0_Sns_Timestamp',
    'Records_0_Sns_SignatureVersion',
    'Records_0_Sns_Signature',
    'Records_0_Sns_SigningCertUrl',
    'Records_0_Sns_UnsubscribeUrl',
    'Records_0_Sns_MessageAttributes_accountId_Type',
    'Records_0_Sns_MessageAttributes_accountId_Value',
    'Records_0_Sns_MessageAttributes_eventName_Type',
    'Records_0_Sns_MessageAttributes_eventName_Value'
]

 # myNest.values()
 Will return: [
     'aws:sns',
    1.0,
    'arn:aws:sns:us-east-1:546754328912:aws-ec2-runinstances:5e378273-4e5d-422f-8058-c9a94703e39c',
    'Notification',
    '816d7f5c-c290-5dbe-85fe-2db22b0d4308',
    'arn:aws:sns:us-east-1:546754328912:aws-ec2-runinstances',
    None,
    0,
    'c4b25530-80f2-5d79-7de1-806bc32c8b3d',
    'AWS API Call via CloudTrail',
    'aws.ec2',
    546754328912,
    '2018-02-02T22:33:05Z',
    'us-east-1',
    1.05,
    'AssumedRole',
    'AROAIBPZGA5H2JMAKH3DM:LANIERK',
    'arn:aws:sts::546754328912:assumed-role/platform--platform/LANIERK',
    546754328912,
    'ASIAJFA7WV5DZ745WQDQ',
    False,
    '2018-02-02T22:26:51Z',
    'Role',
    'AROAIBPZGA5H2JMAKH3DM',
    'arn:aws:iam::546754328912:role/-platform',
    546754328912,
    '-platform',
    '2018-02-02T22:33:05Z',
    'ec2.amazonaws.com',
    'RunInstances',
    'us-east-1',
    '165.225.34.106',
    'console.ec2.amazonaws.com',
    'ami-603b1c1a',
    1,
    1,
    'KyleLanierTest',
    't2.micro',
    '/dev/sda1',
    30,
    True,
    'gp2',
    'xvdca',
    'xvdcb',
    'xvdcc',
    'xvdcd',
    'xvdce',
    'xvdcf',
    'xvdcg',
    'xvdch',
    'xvdci',
    'xvdcj',
    'xvdck',
    'xvdcl',
    'xvdcm',
    'xvdcn',
    'xvdco',
    'xvdcp',
    'xvdcq',
    'xvdcr',
    'xvdcs',
    'xvdct',
    'xvdcu',
    'xvdcv',
    'xvdcw',
    'xvdcx',
    'xvdcy',
    'xvdcz',
    'default',
    False,
    False,
    'stop',
    0,
    'subnet-96294bbb',
    'Primary network interface',
    True,
    'sg-e6fc1d9a',
    0,
    False,
    'instance',
    'BLC',
    1539,
    'CostCenter',
    54111,
    'Name',
    'KyleLanierTagTesting',
    'Owner',
    'cloudengineering@testing.com',
    'volume',
    'BLC',
    1539,
    'CostCenter',
    54111,
    'Name',
    'KyleLanierTagTesting',
    'Owner',
    'cloudengineering@testing.com',
    'standard',
    'ef3e38cb-7772-4840-9fc6-f345d8767a24',
    'r-0cee6e22ba20abc4b',
    546754328912,
    'i-0a626ccee68ff585c',
    'ami-603b1c1a',
    0,
    'pending',
    'ip-10-225-249-73.ec2.internal',
    'KyleLanierTest',
    0,
    't2.micro',
    1517610785000,
    'us-east-1b',
    'default',
    'windows',
    'disabled',
    'subnet-96294bbb',
    'vpc-102e8276',
    '10.225.249.73',
    'pending',
    'pending',
    'x86_64',
    'ebs',
    '/dev/sda1',
    'hvm',
    'xen',
    'BLC',
    1539,
    'CostCenter',
    54111,
    'Name',
    'KyleLanierTagTesting',
    'Owner',
    'cloudengineering@testing.com',
    'sg-e6fc1d9a',
    'Allow All',
    True,
    'eni-2a62d5e7',
    'subnet-96294bbb',
    'vpc-102e8276',
    'Primary network interface',
    546754328912,
    'in-use',
    '12:1e:c2:a1:b7:a8',
    '10.225.249.73',
    'ip-10-225-249-73.ec2.internal',
    True,
    'sg-e6fc1d9a',
    'Allow All',
    'eni-attach-cfe88002',
    0,
    'attaching',
    1517610785000,
    True,
    '10.225.249.73',
    'ip-10-225-249-73.ec2.internal',
    True,
    False,
    'ef3e38cb-7772-4840-9fc6-f345d8767a24',
    '20874fa9-d1ae-4e91-bec3-382bb426360a',
    'AwsApiCall',
    '2018-02-02T22:34:05.710Z',
    1,
    'MOSzUgv7AgohTgIOBLzGromPN3gEmeYJbpEfXOZNLsrDVuoBfNFmy08q+QMti2fdoqasgHRqPljrXFD4lg0KPcsSnuPOyyGaB4lzVWb79i45fjm0bTtWq+ANQdt/sMqHxqnoBF/o5q130rhMEqcm6x3h4/PCv/KhcWbtSXdU2CAfa5nvul2NHv2zZx6GzWcLrBniyvGBt1muSdIEupBshE+zv0q9pbVIfWymtHigYEvdvYO7xsdm5UDTsEwn86ui4XYTOOaZUgoNNfJuX0GmiVdGtZwtCnjrJkmhFPcrAOwqHk+wYzhhfGnKTmqLeMcYZ0njhuO9zjVErSvcbPVVew==',
    'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-433026a4050d206028891664da859041.pem',
    'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:546754328912:aws-ec2-runinstances:5e378273-4e5d-422f-8058-c9a94703e39c',
    'String',
    546754328912,
    'String',
    'RunInstances'
]

# myNest.MessageAttributes
Will return a set of key value pairs where 'MessageAttributes' is in the keys: {
    'Records_0_Sns_MessageAttributes_accountId_Type': 'String',
    'Records_0_Sns_MessageAttributes_accountId_Value': 546754328912,
    'Records_0_Sns_MessageAttributes_eventName_Type': 'String',
    'Records_0_Sns_MessageAttributes_eventName_Value': 'RunInstances'
    }

# myNest.eventName_Value
Will return just the value if only one key contains the string 'eventName_Value': 
    'RunInstances'


# for loop
for k, v in myNest.privateIpAddressesSet.items():
    print('{}: {}'.format(k, v))

Will print:
Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_privateIpAddress: 10.225.249.73
Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_privateDnsName: ip-10-225-249-73.ec2.internal
Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_primary: True

# for loop
for k, v in myNest['privateIpAddressesSet'].items():
    print('{}: {}'.format(k, v))

Will print:
Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_privateIpAddress: 10.225.249.73
Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_privateDnsName: ip-10-225-249-73.ec2.internal
Records_0_Sns_Message_detail_responseElements_instancesSet_items_0_networkInterfaceSet_items_0_privateIpAddressesSet_item_0_primary: True

```

