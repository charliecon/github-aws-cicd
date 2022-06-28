terraform {
    required_providers {
        genesyscloud = {
            source = "mypurecloud/genesyscloud"
        }
    }
}

provider "genesyscloud" {
    sdk_debug  = true
    aws_region = "us-east-1"
}