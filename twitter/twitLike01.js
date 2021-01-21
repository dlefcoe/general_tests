
// did not use this although i could have.


var Twitter = require('twitter');
var config = require('./configTwittLike.js');


var T = new Twitter(config);

var loopTime = 60 * 60 * 1000;   // every 60 minutes

var queryArr = ['#btc','#bitcoin', '#eth'];
queryArr.push('#ftse','#ftse100', 'ftse250','#aim');
// queryArr.push('#bdev', '$kaz', '#sbry', '$bur','$aal','$vrx');
queryArr.push('$fb', '$goog', '$amzn', '$tsla', '$aapl');
queryArr.push('#oott', '#crude', '#copper', '#Lithium');
queryArr.push('#ev', '#javascript', '#nodejs','#py');
queryArr.push('#economy', 'physics','china');
queryArr.push('#fixedincome','#bonds', '#ishares', '#etf', '#earnings');

// Set up your search parameters
var params = {
    q: '#BTC',       // this is the search query
    count: 1,
    result_type: 'recent',
    lang: 'en'
}


console.log("script cycle to run every " + loopTime/60/1000 + " minutes");
console.log("the query array is of size: ", queryArr.length);
console.log("number of get requests per cycle: ", queryArr.length * params.count);
  

var nRuns = 0;
setInterval(function () {
    // this gets run every x minutes
    nRuns++;

    queryArr.forEach(element => {
        params.q = element;
        runTwitter(params);
    });
    
    console.log('number of success script runs: ', nRuns);
    // only post every 10 passes
    if (nRuns%50 == 0) {
        postAtweet("javascript like loop number: " + nRuns + "\n" + "done");    
    }

    
    
},  loopTime); // 16 minutes





function runTwitter(params) {
    T.get('search/tweets', params, function(err, data, response) {
    if(!err){
        // This is where the magic will happen
        var tweetCounter = 0;
        // Loop through the returned tweets
        for(let i = 0; i < data.statuses.length; i++){
            // Get the tweet Id from the returned data
            let id = { id: data.statuses[i].id_str }
            // Try to Favorite the selected Tweet
            T.post('favorites/create', id, function(err, response){
            // If the favorite fails, log the error message
            if(err){
                // if(err[0].message == "You have already favorited this status."){
                //     // do not log to console
                //     tweetCounter++;  
                // }else if(err.message == "HTTP Error: 429 Too Many Requests"){
                //     // too many requests
                //     console.log(err.message);
                //     return;
                // }else{
                //     console.log(err[0].message);}
                tweetCounter++;
                // console.log("some form of error: ", tweetCounter);
                console.log(err);
                
                                
            }
            // If the favorite is successful, log the url of the tweet
            else{
                let username = response.user.screen_name;
                let tweetId = response.id_str;
                console.log('Favorited: ', `https://twitter.com/${username}/status/${tweetId}`)
            }
            console.log("tweet counter:", tweetCounter);  
            });      
        }
        
        
    } else {
        console.log(err);
    }

    })

  
    var tweetText = "DL twit machine has run at time: " + Math.round(Date.now()/1000);
    console.log(tweetText);

}




function postAtweet(tweetText) {
    T.post('statuses/update', {status: tweetText}, function(error, tweet, response) {
    if (!error) {
        console.log("tweet was dome >>>");
        console.log(tweetText);
        console.log(tweet);
    }
    });    
}









