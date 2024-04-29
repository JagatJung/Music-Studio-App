document.getElementById('toggleSidebar').addEventListener('click', function() {
    document.querySelector('aside').classList.toggle('-translate-x-full');
    document.getElementById('main').classList.toggle("md:ml-64");
});


$(document).ready(function() {
    const getUrl = window.location.href;
    const parts = getUrl.split("/");

    $('#view_table').DataTable({
        dom: 'B<"top"f>rt<"bottom"ilp><"clear">', 
        buttons: [
            {
                text: 'Add',
                className: 'my-custom-button', 
                action: function (e, dt, node, config) {
                    register.showModal();
                }
            }, (parts[3] === 'artist') ? 'csv':''
        ]
    });
    
    $('#customButton').on('click', function() {
        $('.buttons-csv').click(); 
    });

    document.getElementById('view_table_length').classList.add("pt-2");
    document.getElementById('view_table_length').classList.add("ml-2");

    const labelElement = document.getElementById('view_table_length').getElementsByTagName('label')[0];
    var textNodes = labelElement.childNodes;
        
    // Iterate over the text nodes
    for (var i = 0; i < textNodes.length; i++) {
        // Check if the text node contains "Show"
        if (textNodes[i].nodeType === Node.TEXT_NODE && textNodes[i].textContent.trim() === "Show") {
            // Replace "Show" with the desired string
            textNodes[i].textContent = "     |  Show ";
            break; // Exit the loop after replacing the first occurrence
        }
    }

    if (getUrl.includes('artist/artist_music')){
        const element_modal = document.getElementsByClassName("artist_select_modal");
        const lastPart = parts[parts.length - 2];
        const lastInteger = parseInt(lastPart);
        element_modal[0].value = lastInteger; 
        element_modal[1].value = lastInteger; 
        element_modal[0].style.display = 'none';
        element_modal[1].style.display = 'none';

        const csv_button = document.getElementsByClassName("buttons-csv");
        csv_button[0].style.display = 'none';

        const element_table = document.getElementsByClassName("artist_column");
        for (let i = 0; i < element_table.length; i++) {
            element_table[i].hidden = true;
        }
    } 

    

});





function showModalCustom(user_id) {
    update.showModal();
    document.getElementById('first_name_modal').value = ((document.getElementById('name_'+user_id).innerText).split(" "))[0];
    document.getElementById('last_name_modal').value = ((document.getElementById('name_'+user_id).innerText).split(" "))[1];
    document.getElementById('dob_modal').value = document.getElementById('dob_'+user_id).innerText;
    document.getElementById('email_modal').value = document.getElementById('email_'+user_id).innerText;
    document.getElementById('phone_modal').value = document.getElementById('phone_'+user_id).innerText;
    
    document.getElementById('gender_modal').value = 
        (document.getElementById('gender_'+user_id).innerText == "Male") ? "m" 
        : (document.getElementById('gender_'+user_id).innerText == "Female") ? "f" 
        : "o" ;
    
    document.getElementById('address_modal').value = document.getElementById('address_'+user_id).innerText;
    document.getElementById('modal_submit').value = 'update_'+user_id;
}

function showModalArtist(artist_id) {
    update.showModal();

    document.getElementById('csv_uploader').style.display = 'none';
    document.getElementById('name_modal').value = document.getElementById('name_'+artist_id).innerText;
    document.getElementById('dob_modal').value = document.getElementById('dob_'+artist_id).innerText;
    document.getElementById('gender_modal').value = 
    (document.getElementById('gender_'+artist_id).innerText == "Male") ? "m" 
    : (document.getElementById('gender_'+artist_id).innerText == "Female") ? "f" 
    : "o" ;
    document.getElementById('address_modal').value = document.getElementById('address_'+artist_id).innerText;
    document.getElementById('no_of_album_modal').value = document.getElementById('noa_'+artist_id).innerText;
    document.getElementById('first_release_modal').value = document.getElementById('debut_'+artist_id).innerText;
    document.getElementById('modal_submit').value = 'update_'+artist_id;
}

function showModalSong(song_id) {
    update.showModal();

    document.getElementById('title_modal').value = document.getElementById('title_'+song_id).innerText;
    document.getElementById('album_name_modal').value = document.getElementById('album_'+song_id).innerText;
    
    document.getElementById('genre_modal').value = 
    (document.getElementById('genre_'+song_id).innerText == "Rhythm and blues") ? "rnb" 
    : (document.getElementById('genre_'+song_id).innerText == "Country") ? "country" 
    : (document.getElementById('genre_'+song_id).innerText == "Classic") ? "classic" 
    : (document.getElementById('genre_'+song_id).innerText == "Rock") ? "rock"
    : "jazz" ;


    document.getElementById('artist_select_modal').value = document.getElementById('name_'+song_id).getAttribute("value");
    
    document.getElementById('modal_submit').value = 'update_'+song_id;
}