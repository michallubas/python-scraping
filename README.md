# Test scraping python
## Before starting
 * Fork the project in your Gitlab namespace
 * **Caution! very important:** Change project visibility: 
   * Click on `Settings` bottom left, when you see your project 
   * Select `General`
   * Click on expend `Visibility, project features, permissions` 
   * Change project visibility from public to private
## After pushing your code
 * Add it@dataimpact.fr as **reporter** in `members`
 * Answer the email with your project link in it 
 
# Test

### All tests are mandatory and requisite for completion.

Some really important tips:
 * Do not change the repository's structure
 * Comments and code quality are a big plus
 * You need to implement unit tests whenever it is possible
 * You might need pytest (and you can use any other package)


## First part

### Task1:

Given a list of keywords, find the longest most recurrent sequence of characters that appears in these keywords.

for example `['milk', 'catalog', 'c+', 'python', 'cat', 'dog']` the result value should be `cat`.

Knowing that you shouldn't use any other list to store the sequences separately.

### Task2:

Given a text containing nutritional values and other properties of a product, Build a dict, having nutrition names as keys and nutrition values including the unit as dict values.
```
Additifs nutritionnels : Vitamine C-D3 : 160 UI, Fer (3b103) : 4mg, Iode (3b202) : 0,28 mg, Cuivre (3b405, 3b406) : 2,2 mg,Manganèse (3b502, 3b503, 3b504) : 1,1 mg, Zinc (3b603,3b605, 3b606) : 11 mg –Clinoptilolited’origine sédimentaire : 2 g. Protéine : 11,0 % - Teneur en matières grasses : 4,5 % - Cendres brutes : 1,7 % - Cellulose brute : 0,5 % - Humidité : 80,0 %.
```
#### The desired output:
```
{"Vitamine C-D3": "160 UI", "Fer (3b103)": "4mg",...}
```

### Task3:

Create a function to check if a list is a grandma list or not, a grandma list is a list of numbers having the product of two or more adjacent numbers in one of its nested lists.
Keep in mind that numbers could only be adjacent if they belong to the same innermost list. In the first example below, the first two numbers(1,2) are adjacent but the first three(1,2,4) aren't.
Example:
```
[1, 2, [[4, 5], [4, 7]], 5, 4, [[95], [2]]]  is grandma list because [2] contains the product 1 * 2
[5, 9, 4, [[8, 7]], 4, 7, [[5]]] is not a grandma list
```

## Second part

### Task1:

Implement a function called http_request that sends a GET request to the following URL: 'https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=1'.

It is important to note that the expected response should contain a success message in JSON format. If the initial request does not yield a 200 response code along with the expected JSON response, please refine your request until it meets these criteria.

### Task2:

Given this curl, update it to make sure it will result in a successful HTTP 2XX response.
```
curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=2
```

### Task 3:

* Write a function that obtains the date for the first day of the last week(not to be confused with previous week) in the current month.
    * Example: The last week if the current month is Feb 2024 would be from Feb 26 to 29
* Apply a decorator to this function so that it formats the date as 'yyyy-mm/d'.

### Task 4:

Write the tests for the class `CacheDecorator` without touching it, some of your tests should not pass because this class is a little buggy. 

### Task 5:
Update `LoginMetaClass` in order to raise an exception each time a method from the class `AccessWebsite` is called while not logged in.
Updating the `AccessWebsite` class isn't allowed.

## Third part

### Task 1:

In the presence of a JSON file named ```third_part/categories.json.gz``` your task is to read its contents and 
build a recursive function capable of returning all categories and subcategories, mirroring the structure outlined in ```third_part/expected_categories.json```.


###### P.S :
  * Use any package to read the json file.

### Task 2:

In the third_part folder, start a new scrapy project and build a spider that crawls the webpage below,
extracting the products names, and the breadcrumb in a list format. Make sure to take
advantage of Scrapy.Items to output the products.
Test your spider and save the results in a csv file.
Webpage:
```
https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas
```
Breadcrumb :
```
Home > Drinks > Cordials, Juices & Iced Teas > Iced Teas
```
The desired format:
```
[“Home”, “Drinks”, “Cordials, Juices & Iced Teas”, “ Iced Teas”]
```

### Task 3:

Same question as Task 2, this time for this URL
```
https://www.edeka24.de/Lebensmittel/Suess-Salzig/Schokoriegel/
```
