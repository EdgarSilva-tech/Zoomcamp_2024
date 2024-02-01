variable "credentials" {
  description = "My Credentials"
  default     = "C:/Users/edgar/OneDrive/Ambiente de Trabalho/AI_Projects/Data Engineering ZoomCamp/week_1/dtc-de-zc-411708-f3b08fce1cc3.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project" {
  description = "Project"
  default     = "dtc-de-zc-411708"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "eu-west6"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default     = "dtc_de_zm_2024_nyc_trips_data"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default     = "dtc-de-zc-411708_nyc_trips_data"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}