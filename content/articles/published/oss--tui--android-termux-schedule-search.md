Title: Craigslist Alerts on Mobile with Termux 
Category: oss/tui
Tags: contribution,android-termux
Gallery: {photo}/craigslist-notify
Status: published

Automation on Android is simplified by Termux, which provides Python and a host device API. 

As a user of the [Craigslist service](/the-case-of-craigslist.html), one function that the website or mobile app did not provide for a long time was saved searches & alerts (it now does). So, I implemented it myself as an experiment with [`Termux:API`](https://f-droid.org/en/packages/com.termux
.api/).

First, install the dependencies and script.

<pre><code class="bash" id="craigslist-notify-deps"></code></pre>

<pre><code id="script" class="bash inline">$ pkg install termux-api openssl libxml2 libxslt
$ pip install https://www.github.com/rwev/craigslist_notify/archive/master.zip
</code></pre>

Some of them may seem out of place or irrelevant for a small Python script, but Termux provides a bare-bones Linux environment by default.

Configure searches by adding a <code id="script" class="bash inline">~/.craigslist_notify_config.yaml</code> containing YAML list items in the following format:

<pre><code id="script" class="yaml inline">- region: '<REGION>' # region to search, as appears in query subdomain, eg. <REGION>.craiglist.org
  query: '<QUERY>' # string as you would enter in search box
  by: 'OWNER' # | 'DEALER' | 'ALL' 
</code></pre>

Once installed and configured, kick off the alert cycle by running <code id="script" class="bash inline">$ craigslist_notify</code>. 
 
On startup, the configured searches are loaded from <code id="script" class="bash inline">~/.craigslist_notify_config.yaml</code>, as and previously known results from <code id="script" class="bash inline">~/.craigslist_notify_state.yaml</code>. For each search, a URL is assembled from the
 various fields. The page is requested and then parsed for listing results. Previously known results are filtered out by ID. All of this, in code:

<pre><code id="main.py" class="python"></code></pre>
<script>
    fetchAndHighlightCodeElement(
        {
            elementId: "main.py",
            fileUrl: "https://raw.githubusercontent.com/rwev/craigslist_notify/master/craigslist_notify/main.py",
            startLine: 126,
            endLine: 144,
            removeEmptyLines: false
        }
    );
</script>

<br>

<pre><code id="request.py" class="python"></code></pre>
<script>
    fetchAndHighlightCodeElement(
        {
            elementId: "request.py",
            fileUrl: "https://raw.githubusercontent.com/rwev/craigslist_notify/master/craigslist_notify/main.py",
            startLine: 96,
            endLine: 125,
            removeEmptyLines: false
        }
    );
</script>

For each new search result, an Android notification is generated over the <code id="script" class="bash inline">termux-notification</code>, which links to the listing in the browser when opened. 
 
<pre><code id="termux_notification.py" class="python"></code></pre>
<script>
    fetchAndHighlightCodeElement(
        {
            elementId: "termux_notification.py",
            fileUrl: "https://raw.githubusercontent.com/rwev/craigslist_notify/master/craigslist_notify/main.py",
            startLine: 70,
            endLine: 82
        }
    );
</script>

After all searches have completed and the results processed, the statefile is updated to save the latest listing IDs as known. 

Just before exit, the script schedules itself to run again in a specified time interval via <code id="script" class="bash inline">termux-job-scheduler
</code>.

<pre><code id="termux_schedule.py" class="python"></code></pre>
<script>
    fetchAndHighlightCodeElement(
        {
            elementId: "termux_schedule.py",
            fileUrl: "https://raw.githubusercontent.com/rwev/craigslist_notify/master/craigslist_notify/main.py",
            startLine: 84,
            endLine: 94
        }
    );
</script>

See the screenshots below for a demonstration. 

The full source code is available at [rwev/craigslist_notify](https://github.com/rwev/craigslist_notify/).

<script>
    highlightInlineCode();  
</script>