<!DOCTYPE html>
<html class="writer-html5" lang="en" >
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="description" content="None" /><link rel="canonical" href="http://127.0.0.1:8000/" />
      <link rel="shortcut icon" href="img/favicon.ico" />
    <title>CCD</title>
    <link rel="stylesheet" href="css/theme.css" />
    <link rel="stylesheet" href="css/theme_extra.css" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/styles/github.min.css" />
        <link href="assets/_mkdocstrings.css" rel="stylesheet" />
    
      <script>
        // Current page data
        var mkdocs_page_name = "Home";
        var mkdocs_page_input_path = "index.md";
        var mkdocs_page_url = "/";
      </script>
    
    <script src="js/jquery-3.6.0.min.js" defer></script>
    <!--[if lt IE 9]>
      <script src="js/html5shiv.min.js"></script>
    <![endif]-->
      <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/highlight.min.js"></script>
      <script>hljs.initHighlightingOnLoad();</script> 
</head>

<body class="wy-body-for-nav" role="document">

  <div class="wy-grid-for-nav">
    <nav data-toggle="wy-nav-shift" class="wy-nav-side stickynav">
    <div class="wy-side-scroll">
      <div class="wy-side-nav-search">
          <a href="." class="icon icon-home"> CCD
        </a><div role="search">
  <form id ="rtd-search-form" class="wy-form" action="./search.html" method="get">
      <input type="text" name="q" placeholder="Search docs" title="Type search term here" />
  </form>
</div>
      </div>

      <div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="Navigation menu">
              <ul class="current">
                <li class="toctree-l1 current"><a class="reference internal current" href=".">Home</a>
    <ul class="current">
    <li class="toctree-l2"><a class="reference internal" href="#commands">Commands</a>
    </li>
    <li class="toctree-l2"><a class="reference internal" href="#project-layout">Project layout</a>
    </li>
    <li class="toctree-l2"><a class="reference internal" href="#brief-overview">Brief Overview</a>
    </li>
    <li class="toctree-l2"><a class="reference internal" href="#group-strengths-and-weaknesses">Group Strengths and Weaknesses</a>
    </li>
    </ul>
                </li>
              </ul>
      </div>
    </div>
    </nav>

    <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap">
      <nav class="wy-nav-top" role="navigation" aria-label="Mobile navigation menu">
          <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
          <a href=".">CCD</a>
        
      </nav>
      <div class="wy-nav-content">
        <div class="rst-content"><div role="navigation" aria-label="breadcrumbs navigation">
  <ul class="wy-breadcrumbs">
    <li><a href="." class="icon icon-home" alt="Docs"></a> &raquo;</li>
      <li>Home</li>
    <li class="wy-breadcrumbs-aside">
    </li>
  </ul>
  <hr/>
</div>
          <div role="main" class="document" itemscope="itemscope" itemtype="http://schema.org/Article">
            <div class="section" itemprop="articleBody">
              
                <h1 id="welcome-to-commidity-correlation-tracker">Welcome to Commidity Correlation Tracker</h1>
<h2 id="commands">Commands</h2>
<ul>
<li><code>1. python main.py</code> - create the required API calls, CSV files, and formatted/melted files </li>
<li><code>2. create_table.py</code> - Start the postgresSQL functions to upload formatted tables into SQL</li>
<li><code>3. dbt run</code> - Run dbt to upload data into pgAdmin4</li>
<li>
<p><code>4. dbt tests</code> - Run dbt tests</p>
<p>main.py - start here and run "python main.py" in order to generate the proper CSV files, "melted_commodity_prices.csv"
create_table.py  - run this after to initlialize the data for use in postgressql</p>
</li>
</ul>
<h2 id="project-layout">Project layout</h2>
<p>Listed below are the model functions we wrote to test our implementation of our API, postgresql, and dbt</p>
<hr />
<p>489856-489215-487404/</p>
<pre><code>main/my_project/target/

            /compiled/

                models/

                    5YCorn.sql  #takes the most recent 5 year prices of corn against the the months the correspond with

                    5YCotton.sql #takes the most recent 5 year prices of cotton against the the months the correspond with

                    5YWheat.sql #takes the most recent 5 year prices of wheat against the the months the correspond with

                    5YWheatvsCorn.sql  #takes the most recent 5 year prices of wheat vs corn and finds the correlation of the two

                    5Ycorrelation.sql #finds the 5 year correlation of wheat vs. corn price over a 5y period

                    5yearmodel.sql #our reference - we use this to pull all commodities prices over the last 5 years

                    AverageCottonvsWheatCorr.sql #calculates the AVERAGE correlation on a 3 month timeframe of Cotton vs. Wheat

                    CornVsWheat.sql #calculates the correlation on a 3 month timeframe of Corn vs. Wheat

                    CottonvsWheat.sql #calculates the correlation on a 3 month timeframe of Cotton vs. Wheat

                    model1.sql #all data from table, should we need it
</code></pre>
<h2 id="brief-overview">Brief Overview</h2>
<p>Our ETL pipeline starts when we pull commodity data from alphaVantage API - here we are pulling ALL data we can on the following commodities:</p>
<p>-Brent Oil
-Crude Oil
-Corn
-Cotton
-Wheat</p>
<p>In this program, we are looking to extract the correlations between any combinations of the commodities, so that statistically better predictions of one 
commodity could be made with information about a correlating commodity. Once we have this data, we format, melt, and export the dataframe with pandas into 
postgreql, which is then inserted into a localhost sql database which allows for us to pull data and correlations quicker than we could otherwise in python.</p>
<p>One serious bottleneck we have is that not all of the commodities were listed in the same year (or decade), so we are starting at the year 1990, when all of the five commodities were officially listed on publically traded exchanges held in alphaVantage's database. </p>
<p>We are more interested in the last five years of data, because though we are not macroeconomic experts, we think it would be fair to start from a time period where COVID affected many aspects of the stock market.</p>
<p>Another bottleneck in our ETL pipeline is the fact that we are only uploading it via .csv file with postgresql. If we were set on having this program be the fastest version of itself, we would likely use bulk insert statements, or directly taking data from the api into our server. We will likely get this working for the last part of our project. </p>
<p>For our DAG, we think that there could be a bottleneck in the way we have to pull five years of data each time we want to run statistical comparisons on prices, which we attempted to solve by using the {{ ref ('xxx') }} command in DBT.</p>
<h2 id="group-strengths-and-weaknesses">Group Strengths and Weaknesses</h2>
<p>Our group broke up the project very evenly - however was not able to meet in person synchronously as much as we would have liked. Michael implemented the postgresql, and Jon and I (Tom) implemented DBT implementations and modules. I think if we were all more flexible on time (as this is the reason it was split by postgres/dbt), I think we would have all worked on each part together more comprehensively. On top of this, we ran into some troubles installing pgAdmin4, which resulted in Jon and I (Tom) using liveshare to work and submit our work. For the future parts of the project, we will likely carve out time in all of our schedules to work on this so that we can all have greater understanding of postgresql, dbt, and mkdocs. </p>
<p>As for strengths, I think that we all have a more thorough undrestanding of the individual topics we did cover (dbt, postgres) because of our need to implement them separately.</p>
<p>Thank you so much, and please feel free to contact us if you have any questions.</p>
              
            </div>
          </div><footer>

  <hr/>

  <div role="contentinfo">
    <!-- Copyright etc -->
  </div>

  Built with <a href="https://www.mkdocs.org/">MkDocs</a> using a <a href="https://github.com/readthedocs/sphinx_rtd_theme">theme</a> provided by <a href="https://readthedocs.org">Read the Docs</a>.
</footer>
          
        </div>
      </div>

    </section>

  </div>

  <div class="rst-versions" role="note" aria-label="Versions">
  <span class="rst-current-version" data-toggle="rst-current-version">
    
    
    
  </span>
</div>
    <script>var base_url = '.';</script>
    <script src="js/theme_extra.js" defer></script>
    <script src="js/theme.js" defer></script>
      <script src="search/main.js" defer></script>
    <script defer>
        window.onload = function () {
            SphinxRtdTheme.Navigation.enable(true);
        };
    </script>

<script>
var livereload = function(epoch, requestId) {
    var req = new XMLHttpRequest();
    req.onloadend = function() {
        if (parseFloat(this.responseText) > epoch) {
            location.reload();
            return;
        }
        var launchNext = livereload.bind(this, epoch, requestId);
        if (this.status === 200) {
            launchNext();
        } else {
            setTimeout(launchNext, 3000);
        }
    };
    req.open("GET", "/livereload/" + epoch + "/" + requestId);
    req.send();

    console.log('Enabled live reload');
}
livereload(105324109, 105324593);
</script></body>
</html>

<!--
MkDocs version : 1.4.2
Build Date UTC : 2023-04-07 22:21:32.793180+00:00
-->
