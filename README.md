# Open-Redirect-Finder

<p><strong>Open Redirect Finder</strong> is an automation tool used to detect open redirect vulnerabilities on a URL.</p>

![Open-Redirect-Finder Jenderal92](https://github.com/user-attachments/assets/33e3aef8-40e8-45f7-b62a-ce76265ff04b)


## Features

<ul>
    <li>Batch Processing: Supports testing multiple URLs at once from an input file.</li>
    <li>Automatic Validation: Checks whether the entered URLs are vulnerable to open redirects.</li>
    <p>Payload Options:</p>
    <li>Default Payload (Option 1): Uses only the payload provided in the code.</li>
    <li>Custom Payload (Option 2): Uses a custom payload entered by the user through the <code>custom.txt</code> file.</li>
    <li>Combine Default and Custom Payload (Option 3): Uses a combination of both default and custom payloads.</li>
</ul>

## How to Use

<ol>
    <li>
        <p><strong>Download and Install Python</strong></p>
        <p>Ensure Python 2.7 is installed on your system. You can download it from the official Python website: 
        <a href="https://www.python.org" target="_blank">https://www.python.org</a>.</p>
    </li>
    <li>
        <p><strong>Install Required Module</strong></p>
        <p>Run the following command to install the <code>requests</code> library:</p>
        <pre>pip install requests</pre>
    </li>
    <li>
        <p><strong>Prepare the Target URL File</strong></p>
        <p>Prepare a text file containing a list of target URLs (e.g., <code>urls.txt</code>). Each URL should be on a separate line.</p>
    </li>
    <li>
        <p><strong>Select Payload Option</strong></p>
        <p>Choose the payload option you would like to use:</p>
        <ul>
            <li><p><strong>Option 1</strong>: Use the default payload that is already provided by the tool.</p></li>
            <li><p><strong>Option 2</strong>: Use a custom payload that you create, such as from the <code>custom.txt</code> file.</p></li>
            <li><p><strong>Option 3</strong>: Combine the default and custom payloads for a more comprehensive test.</p></li>
        </ul>
    </li>
    <li>
        <p><strong>Follow the Results</strong></p>
        <p>After selecting the payload and starting the test, follow the results displayed in the terminal. If an open redirect vulnerability is found, the vulnerable URL will be shown along with the payload used to discover it.</p>
    </li>
    <li>
        <p><strong>Save the Test Results</strong></p>
        <p>The test results will be saved in the <code>results.txt</code> file. This file contains a list of vulnerable URLs along with the payload used to exploit the open redirect vulnerability.</p>
    </li>
</ol>

## Disclaimer !!!

<p>I have written the disclaimer on the cover of Jenderal92. You can check it <a href="https://github.com/Jenderal92">HERE !!!</a></p>
