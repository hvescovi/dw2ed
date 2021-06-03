/ex01/build/classes$ jar -cvmf ../../manifesto.txt ex01.jar jnlpexample01/JNLPExample01.class 
added manifest
adding: jnlpexample01/JNLPExample01.class(in = 1295) (out= 796)(deflated 38%)




(the password is: friend)

$:~/01-github/dw2ed/sup/java/jnlp/ex01$ keytool -genkey -keystore testkeys -alias stathis
Enter keystore password:  
Re-enter new password: 
What is your first and last name?
  [Unknown]:  Hylson Netto
What is the name of your organizational unit?
  [Unknown]:  IFC
What is the name of your organization?
  [Unknown]:  IFC
What is the name of your City or Locality?
  [Unknown]:  Blumenau
What is the name of your State or Province?
  [Unknown]:  Santa Catarina
What is the two-letter country code for this unit?
  [Unknown]:  SC
Is CN=Hylson Netto, OU=IFC, O=IFC, L=Blumenau, ST=Santa Catarina, C=SC correct?
  [no]:  yes

$:~/01-github/dw2ed/sup/java/jnlp/ex01$






$:~/01-github/dw2ed/sup/java/jnlp/ex01$ jarsigner -keystore testkeys ex01.jar stathis
Enter Passphrase for keystore: 
jar signed.

Warning: 
The signer's certificate is self-signed.
$:~/01-github/dw2ed/sup/java/jnlp/ex01$





get jnlp from:
http://hylson.com/java/jnlp/


