terraform {
  required_version = ">= 1.7.0"
}

provider "google" {
  project = var.project_id
  region  = var.region
}