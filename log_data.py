wazuh_attackers = [
    "200.174.194.100",
    "200.174.194.101",
    "200.174.194.102",
    "200.174.194.103",
    "200.174.194.104"
]

wazuh_attacker_names = [
    "diana.l",
    "barry.s",
    "guy.b",
    "eric.j",
    "doris.z"
]

nmap_attackers = [
    "223.220.159.150",
    "223.220.150.130",
    "95.215.1.13",
    "200.174.194.101",
    "186.32.225.253",
    "217.117.13.170"
]

nmap_destinations = [
    "165.227.62.167",
     "208.244.250.75",
     "204.8.4.32",
     "163.191.145.137",
     "204.8.4.33",
     "165.227.62.166"
]

nmap_ports = [80, 443, 8080, 4443, 22]

nmap_benigns = [
    "38.21.240.1",
    "192.3.183.186",
    "151.51.227.206",
    "192.85.77.234"
]

nmap_dest_benigns = [
     "165.227.62.167",
     "208.244.250.75",
     "204.8.4.32",
     "163.191.145.137"
]

nmap_ports_benigns = [80, 443, 8080, 22]

ssh_attackers = [
    "223.220.159.150",
    "129.204.58.88",
    "95.215.1.13",
    "193.112.94.86",
    "159.16.96.716"
]

ssh_attacker_names = [
    "john.doe",
    "mike.smith",
    "james.bean",
    "charles.jenkins",
    "margaret.richardson"
]

ssh_user = [
        "ubuntu",
        "dave",
        "lea",
        "gil",
        "ruth"
]

ssh_instance_id = [
       "i-0fb1eaaa86e021111",
       "i-0fb1eaaa86e022222",
       "i-0fb1ebbb86e023333",
       "i-0fb1eaaa86e024444",
       "i-0fb1eaaa86e025555",
]
  
iam_attackers = [
    "223.220.159.150",
    "129.204.58.88",
    "95.215.1.13",
    "95.215.1.15",
    "95.215.1.16"
]

iam_attacker_names = [
    "john.doe",
    "mike.smith",
    "james.bean",
    "charles.jenkins",
    "margaret.richardson"
]

iam_attacker_arn = [
    "arn:aws:iam::486140753397:user/john.doe",
    "arn:aws:iam::486140753397:user/mike.smith",
    "arn:aws:iam::486140753397:user/james.bean",
    "arn:aws:iam::486140753397:user/charles.jenkins",
    "arn:aws:iam::486140753397:user/margaret.richardson"
]

iam_benigns = [
    "38.21.240.1",
    "192.3.183.186",
    "151.51.227.206",
    "192.85.77.234",
    "192.84.78.111"
]

iam_benigns_names = [
    "marie.jean",
    "david.ross",
    "dan.white",
    "jennifer.light",
    "robert.cook"
]

iam_benigns_arn = [
    "arn:aws:iam::486140753397:user/marie.jean",
    "arn:aws:iam::486140753397:user/david.ross",
    "arn:aws:iam::486140753397:user/dan.white",
    "arn:aws:iam::486140753397:user/jennifer.light",
    "arn:aws:iam::486140753397:user/robert.cook"
]

s3_bucket_sensitive = [
    "s3_internaldocs",
    "s3_finance",
    "s3_credentials",
    "s3_medical",
    "s3_critical"
]

s3_bucket_host_sensitive = [
    "s3_internaldocs.s3.amazonaws.com",
    "s3_finance.s3.amazonaws.com",
    "s3_credentials.s3.amazonaws.com",
    "s3_medical.s3.amazonaws.com",
    "s3_critical.s3.amazonaws.com",
]

s3_bucket_benign = [
    "s3_flowers",
    "s3_takeaways",
    "s3_photos",
    "s3_cats",
    "s3_share"
]   

s3_bucket_host_benign = [
    "s3_flowers.s3.amazonaws.com",
    "s3_takeaway.s3.amazonaws.com",
    "s3_photos.s3.amazonaws.com",
    "s3_cats.s3.amazonaws.com",
    "s3_share.s3.amazonaws.com",
]
            
s3_bucket_arn_sensitive = [
    "arn:aws:s3:::s3_internaldocs/salaries",
    "arn:aws:s3:::s3_finance/financial_reports",
    "arn:aws:s3:::s3_credentials/personal_letters",
    "arn:aws:s3:::s3_medical/personal_info",
    "arn:aws:s3:::s3_critical/results_q1"
]

s3_bucket_arn_benign = [
    "arn:aws:s3:::s3_flowers/roses",
    "arn:aws:s3:::s3_takeaways/courses",
    "arn:aws:s3:::s3_photos/cake_photos",
    "arn:aws:s3:::s3_cats/babies",
    "arn:aws:s3:::s3_share/lists"
]

s3_files_sensitive = [
    "salaries",
    "financial_reports",
    "personal_letters",
    "personal_info",
    "results_q1"
]

s3_files_benign = [
    "roses",
    "courses",
    "cake_photos",
    "babies",
    "lists"
]

############################
#
# Story #1 
############################
apache_benigns = [
    "91.90.127.88",
    "91.90.130.1",
    "91.90.130.2",
    "131.4.5.6",
    "131.4.5.7",
]

apache_attacker = [
    "122.174.194.5",
    "95.215.1.222",
    "223.220.150.131"
]

apache_user_agent = [
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
]

px_ip_malicious = [
    "104.238.156.0/24",
    "67.201.56.0/21",
    "103.3.77.0/24"
]
