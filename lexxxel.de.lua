a(_a, "89.58.25.61")
a("*.lexxxel.de", "89.58.25.61")
aaaa(_a, "2a03:4000:62:fd5::1")
aaaa("*.lexxxel.de", "2a03:4000:62:fd5::1")

a("mail.lexxxel.de", "89.58.25.61")
aaaa("mail.lexxxel.de", "2a03:4000:62:fd5::1")
mx(_a, "mail.lexxxel.de", 5)

txt(_a, "v=DKIM1; h=sha256; k=rsa; ", 180)
txt(_a, "p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2epBFWPIc9BtMELPVnX2hPjpZ0AMhRp4aSg+BvywnUV8asVeKsinloYo/QsBz2L1cg4IENz8FSPqwCgxdfvuHNtErO3gZ5UQ7AKi9Mf/mlg197f+w5I3YiRvJDMTOTXO8GX1psLypVwRHYHTptB7JYC4r0j6uvFxA65VQvAc1+2KCP4MBJ1T5NXiRbYPvrau+oAUJwM+qPGnRP", 180)
txt(_a, "Ko7oBlWssUn6P2i09VF3/Ok4fAjPIfbTL/XIZG9enf+3jOVpmSQRxMuYg6yN6oNbZ6Ytq/zKVhTHvyTj8LiBtRqpjZn50fELdhX4zA93hL22n7+rrwRfNoSQoEARdx5iq1pFAevwIDAQAB", 180)

txt(_a, "v=spf1 mx ~all", 180)

txt(concat("_dmarc", _a), "v=DMARC1; p=none; rua=mailto:abuse@lexxxel.de; ruf=mailto:abuse@lexxxel.de; sp=none; ri=86400", 180)

txt(concat("mail", _a), "v=DKIM1; h=sha256; k=rsa; ", 180)
txt(concat("mail", _a), "p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2epBFWPIc9BtMELPVnX2hPjpZ0AMhRp4aSg+BvywnUV8asVeKsinloYo/QsBz2L1cg4IENz8FSPqwCgxdfvuHNtErO3gZ5UQ7AKi9Mf/mlg197f+w5I3YiRvJDMTOTXO8GX1psLypVwRHYHTptB7JYC4r0j6uvFxA65VQvAc1+2KCP4MBJ1T5NXiRbYPvrau+oAUJwM+qPGnRP", 180)
txt(concat("mail", _a), "Ko7oBlWssUn6P2i09VF3/Ok4fAjPIfbTL/XIZG9enf+3jOVpmSQRxMuYg6yN6oNbZ6Ytq/zKVhTHvyTj8LiBtRqpjZn50fELdhX4zA93hL22n7+rrwRfNoSQoEARdx5iq1pFAevwIDAQAB", 180)

txt(concat("mail", _a), "v=spf1 mx ~all", 180)

