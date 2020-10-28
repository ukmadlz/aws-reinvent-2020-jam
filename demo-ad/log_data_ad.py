#
#  Admins
#       "Mike",
#       "Brenda",
#        "Alfred"
#       "Administrator"
#
#  Users
#       "Moris",
#       "Susan",
#       "Diane",
#       "Chris",
#       "Dan",
#       "Tim",
#       "Annie",
#       "Brent"
#
#
# Malicious hacker is using "Administrator" instead of an administrator user name like Danny
#

#  Used by 4720 4722 4725 4625 4724 4726
# "alpha"
#  4625 - The user that logged-in
#  4720 - The account that was created
#  4722 - The user that was enabled
#  4724 - The user whose was reset
#  4725 - The account that was disabled
#  4726 - The account that was deleted
#
# benign
TargetUserName = [
        "MorisL",
        "SusanM",
        "DianeA",
        "ChrisW",
        "DanB",
        "TimH",
        "AnnieL",
        "BrentC"
]

#
#  4720  - The account that was created
#  4720 - SamAccountName is exactly the same as TargetUserName field - use same array
TargetUserNameCreated = [
        "MiaH",
        "NormaG",
        "AlexisY",
        "HeikeC",
        "BradyF",
        "DaphneA",
        "LashonP",
        "MickeyS",
        "MargaretteG"
]

#
# Used by 4720
# "Chris Brown"
#  4720  - The display name of the created account
#
DisplayNameAccountCreated = [
    "Mia Hall",
    "Norma Grubb",
    "Alexis Yen",
    "Heike Cliff",
    "Brady Finn",
    "Daphne Ash",
    "Lashon Petro",
    "Mickey Streight",
    "Margarette Grimaldi"
]

TargetUserNameOld = [
        "JohnGarden"
]

TargetUserNameExists = [
        "KateBall"
]

# Used by 4625  source IP used to login
#
IpAddress = [
    "231.122.87.139",
    "205.194.43.232",
    "159.178.196.22",
    "121.201.218.184",
    "202.207.87.120",
    "116.216.135.83",
    "153.5.78.16",
    "94.92.191.126",
    "178.186.88.12",
    "220.45.253.143"
]

MaliciousIpAddress = [
    "58.213.133.18",
    "175.126.62.151"
]

# 4720 -  Administraor is malicious hacker creating a new User JohnDoe to use it later
TargetUserNamebadadmin = [
        "JohnDoe"
]

DisplayNameBadAdmin = [
    "John Doe"
]

#
# Used by 4624 4720 4722 4724 4725 4726
#  4720 - The admin that created the account
#  4722 - The admin that enabled the account
#  4724 - The admin that did the reset
#  4725 - The admin that disabled the account
#  4726 - The admin that deleted the account
#
SubjectAdminName = [
    "MikeC",
    "BrendaO",
    "AlfredF",
    "MattL"
]

BenignAdminIpAddress = [
    "153.5.78.16",
    "94.92.191.126",
    "178.186.88.12",
    "220.45.253.143"
]

TargetUserNameFreelance = [
    "MosheK",
    "ZeevA",
    "EliK",
    "EveL"
]


BenignIpAddress = [
    "159.178.196.22",
    "121.201.218.184"
]

BenignUserName = [
    "BellaZ",
    "JosephA"
]

BenignUserName2 = [
        "MorisL",
        "SusanM",
        "DianeA",
        "ChrisW"
]

BenignIpAddress2 = [
    "231.122.87.139",
    "205.194.43.232",
    "159.178.196.22",
    "121.201.218.184"
]

#
#  4720  - The account that was created
#  4720 - SamAccountName is exactly the same as TargetUserName field - use same array
TargetUserNameCreated2 = [
        "MiaH",
        "NormaG",
        "AlexisY",
        "HeikeC"
]

DisplayNameAccountCreated2 = [
    "Mia Hall",
    "Norma Grubb",
    "Alexis Yen",
    "Heike Cliff"
]