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