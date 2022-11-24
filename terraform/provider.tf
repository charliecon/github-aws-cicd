terraform {
    required_providers {
        genesyscloud = {
            source  = "mypurecloud/genesyscloud"
            version = "1.9.0"
        }
    }
}

provider "genesyscloud" {
    sdk_debug = true
}