# Valida_NF_market_place
For market place website this application is useful to check, if the third party seller issued the correct invoice.

The application is to analyze invoices, it compare the website sold product description to xml invoice file, to avoid third party seller to issue a invoice with a different description from what was available on website.
This app is useful for example to Amazon.com, MagazineLuiza.com.br and MercadoLivre.com.br.

This project has two folders:
  NFe -> This is to keep invoices files.
  modulos -> There are modules to run the application.

How to run this application:
Basically you've to use the 'search_invoice()' function to analyze if there is any invoice in line to be analyzed.  It will search for the xml file name that it is in line to be checked on invoice_check.db to compare to its invoice. When there is recorded data that the checking column is filled as 'newbie', the search_invoice function has to work. It will get the invoice_id and search a xml file that has the same name. In the end, the application will show on terminal if the invoice is regular or not.
