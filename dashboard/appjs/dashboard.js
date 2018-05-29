/**
 * Created by manuel on 5/8/18.
 */

// Load the Visualization API and the piechart package.
google.charts.load('current', {'packages': ['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

function reformatDataReactions(jsonData){
    var temp= jsonData.Reactions;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        dataElement.push(row.day);
        dataElement.push(row.reactions);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function reformatDataHashtags(jsonData){
    var temp= jsonData.Hashtags;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        dataElement.push(row.hashtag + ' - ' + row.date_created);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function reformatDataMessages(jsonData){
    var temp= jsonData.Messages;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        dataElement.push(row.day);
        dataElement.push(row.number_of_messages);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function reformatDataReplies(jsonData){
    var temp= jsonData.Replies;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        dataElement.push(row.day);
        dataElement.push(row.number_of_replies);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function reformatDataUsers(jsonData){
    var temp= jsonData.Users;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        dataElement.push(row.day);
        dataElement.push(row.active_users);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function drawChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/Reactions/countLikes",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Days');
    data.addColumn('number', 'Likes');
    data.addRows(reformatDataReactions(JSON.parse(jsonData)));

    var options = {
        title: 'Likes per day',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Likes',
            minValue: 0
        },
        vAxis: {
            title: 'Days'
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('likeschart_div'));
    chart.draw(data, options);
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    jsonData = $.ajax({
        url: "http://localhost:5000/Reactions/countDislikes",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

        var data2 = new google.visualization.DataTable();
        data2.addColumn('string', 'Days');
        data2.addColumn('number', 'Dislikes');
        data2.addRows(reformatDataReactions(JSON.parse(jsonData)));

        var options2 = {
            title: 'Dislikes per day',
            chartArea: {width: '50%'},
            hAxis: {
                title: 'Total Dislikes',
                minValue: 0
            },
            vAxis: {
                title: 'Days'
            }
        };



    var chart2 = new google.visualization.BarChart(document.getElementById('dislikeschart_div'));
    chart2.draw(data2, options2);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    jsonData = $.ajax({
        url: "http://localhost:5000/Hashtags/Trends",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data3 = new google.visualization.DataTable();
    data3.addColumn('string', 'Hashtag');
    data3.addColumn('number', 'Number of Uses');
    data3.addRows(reformatDataHashtags(JSON.parse(jsonData)));

    var options3 = {
        title: 'Hashtags per day',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Number of Uses',
            minValue: 0
        },
        vAxis: {
            title: 'Hashtags per day'
        }
    };

    var chart3 = new google.visualization.BarChart(document.getElementById('trendschart_div'));
    chart3.draw(data3, options3);

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    jsonData = $.ajax({
        url: "http://localhost:5000/Messages/count",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    data4 = new google.visualization.DataTable();
    data4.addColumn('string', 'Days');
    data4.addColumn('number', 'Messages');
    data4.addRows(reformatDataMessages(JSON.parse(jsonData)));

    options4 = {
        title: 'Messages per day',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Messages',
            minValue: 0
        },
        vAxis: {
            title: 'Days'
        }
    };

    var chart4 = new google.visualization.BarChart(document.getElementById('messageschart_div'));
    chart4.draw(data4, options4);
///////////////////////////////////////////////////////////////////////////////////////////////////////

    jsonData = $.ajax({
        url: "http://localhost:5000/Messages/Replies/count",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    data5 = new google.visualization.DataTable();
    data5.addColumn('string', 'Days');
    data5.addColumn('number', 'Replies');
    data5.addRows(reformatDataReplies(JSON.parse(jsonData)));

    options5 = {
        title: 'Replies per day',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Replies',
            minValue: 0
        },
        vAxis: {
            title: 'Days'
        }
    };

    var chart5 = new google.visualization.BarChart(document.getElementById('replieschart_div'));
    chart5.draw(data5, options5);

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    jsonData = $.ajax({
        url: "http://localhost:5000/Users/active",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data6 = new google.visualization.DataTable();
    data6.addColumn('string', 'Days');
    data6.addColumn('number', 'Active Users');
    data6.addRows(reformatDataUsers(JSON.parse(jsonData)));

    var options6 = {
        title: 'Active Users per day',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Active Users',
            minValue: 0
        },
        vAxis: {
            title: 'Days'
        }
    };

    var chart6 = new google.visualization.BarChart(document.getElementById('userschart_div'));
    chart6.draw(data6, options6);
}


google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawChart);
//google.charts.setOnLoadCallback(drawChart2);



