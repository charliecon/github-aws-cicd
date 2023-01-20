terraform {
    required_providers {
        genesyscloud = {
            source  = "mypurecloud/genesyscloud"
            version = "1.10.0"
        }
    }
}

provider "genesyscloud" {
    # config options
    sdk_debug = true
}