// Code goes here

function render(data) {
    
            var html = "<div class='commentBox'><div class='rightPanel'><span>" + data.name + "</span><div class='date'>" + data.date + "</div><p>" + data.body + "</p></div><div class='clear'></div></div>";
    
            $('#container').append(html);
    
        }
    
        $(document).ready(function() {
    
            var coment = [{
                "name": "Ece Alptekin",
                "date": "2020-06-01",
                "body": "Excellent!"
            }];
    
            for (var i = 0; i < coment.length; i++) {
                render(coment[i]);
    
            }
    
            $('#addComent').click(function() {
                var addObj = {
                    "name": $('#name').val(),
                    "date": $('#date').val(),
                    "body": $('#bodyText').val()
                };
    
                coment.push(addObj);
                render(addObj);
                $('#name').val('');
                $('#date').val('dd/mm/yyyy');
                $('#bodyText').val('');
            });
        });