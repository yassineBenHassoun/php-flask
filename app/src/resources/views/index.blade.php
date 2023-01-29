<!doctype html>
<html lang="en">
    <head>
        <title>Test Technique - {Nom du candidat}</title>
        <meta charset="utf-8">

        <link rel="stylesheet" href="css/custom.css">
        <script src="https://code.jquery.com/jquery-3.6.1.min.js"></script>
        <script src="js/custom.js"></script>
    </head>
    <body>
       
        <div>
            <canvas id="myChart"></canvas>
        </div>
          
          <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
          
          <script>
            const ctx = document.getElementById('myChart');
          
            new Chart(ctx, {
              type: 'bar',
              data: {
                labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                datasets: [{
                  label: '# of Votes',
                  data: [12, 19, 3, 5, 2, 3],
                  borderWidth: 1
                }]
              },
              options: {
                scales: {
                  y: {
                    beginAtZero: true
                  }
                }
              }
            });
          </script>
           

    </body>
</html>