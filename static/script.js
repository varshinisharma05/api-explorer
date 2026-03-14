$(document).ready(function(){

    // Hide result sections initially
    $('#countryResult').hide();
    $('#weatherResult').hide();
    $('#recipeResult').hide();
    $('#historyResult').hide();
    $('#resultCard').hide();


    // ================================
    // CHANGE INPUT LABEL
    // ================================
    $('#apiSelect').change(function(){

        let api = $(this).val();

        if(api === "country"){
            $('#inputLabel').text("Enter Country Name");
        }
        else if(api === "weather"){
            $('#inputLabel').text("Enter City Name");
        }
        else if(api === "recipe"){
            $('#inputLabel').text("Enter Food Name");
        }

    });


    // ================================
    // RUN API BUTTON
    // ================================
    $('#runBtn').click(function(){

        let input = $('#countryInput').val().trim();
        let api = $('#apiSelect').val();

        if(input === ""){
            alert("Please enter a value");
            return;
        }

        if(!api){
            alert("Please select an API");
            return;
        }

        let url = "";

        if(api === "country"){
            url = "/api/country/" + encodeURIComponent(input);
        }
        else if(api === "weather"){
            url = "/api/weather/" + encodeURIComponent(input);
        }
        else if(api === "recipe"){
            url = "/api/recipe/" + encodeURIComponent(input);
        }

        $('#resultCard').show();
        $('#loadingText').show();

        // Hide previous results
        $('#countryResult').hide();
        $('#weatherResult').hide();
        $('#recipeResult').hide();
        $('#historyResult').hide();

        $.get(url)

        .done(function(data){

            $('#loadingText').hide();

            // ================= COUNTRY =================
            if(api === "country"){

                $('#countryResult').show();

                $('#countryName').text(data.country || "N/A");
                $('#capital').text(data.capital || "N/A");
                $('#region').text(data.region || "N/A");
                $('#population').text(data.population || "N/A");

            }

            // ================= WEATHER =================
            else if(api === "weather"){

                $('#weatherResult').show();

                $('#city').text(data.city || "N/A");
                $('#temperature').text((data.temperature || "-") + " °C");
                $('#weather').text(data.weather || "N/A");
                $('#humidity').text((data.humidity || "-") + "%");

            }

            // ================= RECIPE =================
            else if(api === "recipe"){

                $('#recipeResult').show();
                $('#recipeResult').html("");

                if(!data || data.length === 0){
                    $('#recipeResult').html("<p>No recipes found.</p>");
                    return;
                }

                data.forEach(function(recipe){

                    let card = `
                    <div class="col-md-4 mb-3">
                        <div class="card recipe-card h-100">
                            <img src="${recipe.image}" class="card-img-top" alt="${recipe.name}">
                            <div class="card-body">
                                <h5 class="card-title">${recipe.name}</h5>
                            </div>
                        </div>
                    </div>
                    `;

                    $('#recipeResult').append(card);

                });

            }

        })

        .fail(function(){

            $('#loadingText').hide();

            $('#countryResult').hide();
            $('#weatherResult').hide();
            $('#recipeResult').hide();

            alert("Error occurred while fetching API data.");

        });

    });


    // ================================
    // SEARCH HISTORY BUTTON
    // ================================
    $('#historyBtn').click(function(){

        $('#resultCard').show();
        $('#loadingText').show();

        $('#countryResult').hide();
        $('#weatherResult').hide();
        $('#recipeResult').hide();
        $('#historyResult').show();

        $.get("/api/history")

        .done(function(data){

            $('#loadingText').hide();
            $('#historyList').html("");

            if(!data || data.length === 0){
                $('#historyList').html("<li class='list-group-item'>No history found</li>");
                return;
            }

            data.forEach(function(item){

                let listItem = `
                <li class="list-group-item">
                    <strong>${item.type}</strong> : ${item.query}
                    <br>
                    <small class="text-muted">${item.time}</small>
                </li>
                `;

                $('#historyList').append(listItem);

            });

        })

        .fail(function(){

            $('#loadingText').hide();
            alert("Failed to load history.");

        });

    });

});