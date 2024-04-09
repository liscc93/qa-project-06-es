<h1>Project 6 - begining test automation </h1>

<h2> Description of Project 6 </h2>

<h4>The main objective of this project is to optimize and simplify the testing procedure specifically designed for the "name" field, through the implementation of automation tools. This field, characterized by its variability in the number of characters, as well as the inclusion of special characters and numerals, presents a considerable challenge in terms of manual verification. Consequently, automation becomes an essential resource to streamline this process and ensure its accuracy. Depending on the specific needs of each case, criteria and protocols will be established for the comprehensive validation of the data entered in this field, thus ensuring the integrity and coherence of the information. 

Within this project, both positive and negative tests will be conducted to verify compliance with specifications and ensure successful user creation, while also preventing errors with invalid inputs. Automating these tests minimizes human errors and saves time efficiently.

This project relies on the documentation provided by apiDoc to define the functionality specifications and ensure their consistency with the system requirements.

</h4>

<h2>Steps to run the tests:</h2>

<h3>1. You need to have the pytest and request packages installed to run the tests.</h3>
    <li>First, go to the "Python Packages" option located at the bottom left of PyCharm.</li>
    <li>Second, search for the packages in the search bar.</li>
    <li>Third, install the latest version of the packages.</li>
<h3>2. Run the tests.</h3>
    <li>Ensure that the URL in the configuration.py file is up-to-date.</li>
    <li>Now you can run the tests using the "pytest" command followed by the name of the file containing the tests.</li>

<h2>Verification</h2>

<table>

<tr>
<th> # </th> 
<th> Description </th>
<th> Expected Result (ER): </th>
</tr>

<tr>
<td>1</td>
<td> The allowed number of characters (1): </td>
<td> Response code: 201 </td>
</tr>

<tr>
<td>2</td>
<td> The allowed number of characters (511): </td>
<td> Response code: 201 </td>
</tr>

<tr>
<td>3</td>
<td> The number of characters is less than the allowed amount (0): </td>
<td> Response code: 400 </td>
</tr>

<tr>
<td>4</td>
<td> The number of characters is greater than the allowed amount (512): </td>
<td> Response code: 400 </td>
</tr>

<tr>
<td>5</td>
<td> Special characters are allowed: </td>
<td> Response code: 201 </td>
</tr>

<tr>
<td>6</td>
<td> Spaces are allowed: </td>
<td> Response code: 201 </td>
</tr>

<tr>
<td>7</td>
<td> Numbers are allowed: </td>
<td> Response code: 201 </td>
</tr>

<tr>
<td>8</td>
<td> The parameter is not passed in the request: </td>
<td> Response code: 400 </td>
</tr>

<tr>
<td>9</td>
<td> A different parameter type has been passed (number): </td>
<td> Response code: 400 </td>
</tr>

</table>
