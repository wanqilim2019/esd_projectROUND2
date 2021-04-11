<!DOCTYPE html>
<html lang="en">

<head>
    <?php include "head.html" ?>

    <title>Marketplace</title>
</head>

<body>
    <?php include "nav.html" ?>

    <section id="Header" class="py-2">
        <div class="text-center">

        </div>
    </section>

    <!-- Implementing search bar with Vue -->
    <div id="app">
        <div class='container'>
            <div class="row">
                <div class="col-lg-4 col-md-6 col-sm-12">

                </div>
                <div class="col-lg-4 col-md-6 col-sm-12 text-center">
                    <h1>My Orders</h1>
                </div>
                <div class="container" id="app">
                    <ul class="list-group">

                        <li class="list-group-item">
                            <div class="row">
                                <img class="col-3" src="#" style="border-top-left-radius: 20px;border-top-right-radius: 20px">
                                <div class="col-3">
                                    <h2>pname</h2>

                                    <h5>address </h5>
                                    <h5 id='statusline'>dStatus </h5>
                                </div>
                                <div class="col-2"></div>
                                <div class="col-3">
                                    <h5>datetime</h5>
                                    <h2>Quantity:</h2>
                                    <!-- button to fulfill order -->
                                    <!--  if session['acctType'] == 'business' and d.dStatus == 'Unfulfilled'  -->
                                    <input type="hidden" id="oid" name="oid" value="oid" />
                                    <input type="hidden" id="dstatus" name="dstatus" value="dStatus" />
                                    <button id='submit' class="btn btn-warning">Fulfil Order</button>
                                    <!-- end if -->
                                </div>
                            </div>
                        </li>
                        <!-- end for -->
                    </ul>
                    <!-- else -->
                    <div>
                        <h1>No Orders!</h1>
                        <h2>You have not order anything.</h2>
                        <p><a href=""> Shop here now</a></p>
                    </div>
                    <!-- end if -->

                </div>

            </div>
        </div>
    </div>

    <script type="text/javascript">
        $(document).ready(function() {
            var acctType = sessionStorage.getItem('acctType');


            $('#submit').click(function() {
                console.log("click");
                var oid = String($('#oid').val());
                console.log(oid);
                var dstatus = $('#dstatus').val();
                if (dstatus == 'Unfulfilled') {
                    $.ajax({
                        url: 'http://localhost:5400/fulfill_order', //Your api url
                        type: 'PUT', //type is any HTTP method
                        data: {
                            data: {
                                'oid': oid,
                                'dStatus': 'Fulfilled'
                            }
                        }, //Data as js object
                        success: function() {
                            $('#statusline').innerText = 'Fulfilled';
                        }
                    });
                }

            });
        });
        var business_url = "http://localhost:5100/check_order_biz";
        var customer_url = "http://localhost:5300/check_order_cust";
        var acctType = sessionStorage.getItem('acctType');

        var app = new Vue({
            el: "#app",
            computed: {
                hasOrders: function() {
                    return this.books.length > 0;
                }
            },
            data: {
                isbn13: "",
                books: [],
                message: "There is a problem retrieving books data, please try again later.",
                newTitle: "",
                newISBN13: "",
                newPrice: "",
                newAvailability: "",
                bookAdded: false,
                addBookError: "",
                orderedBook: "",
                orderPlaced: false,
                orderSuccessful: false,
            },
            methods: {
                getAllOrders: function() {
                    console.log('getallorders')
                    if (acctType == 'business') {
                        bid = sessionStorage.getItem('bid');
                        getURL = business_url  + '/'+ bid;
                    } else if (acctType == 'customer') {
                        cid = sessionStorage.getItem('cid');
                        getURL = customer_url + '/'+cid;
                    }
                    const response =
                        fetch(getURL)
                        .then(response => response.json())
                        .then(data => {
                            console.log(response);
                            if (data.code === 404) {
                                // no book in db
                                this.message = data.message;
                            } else {
                                // add codes
                            }
                        })
                        .catch(error => {
                            // Errors when calling the service; such as network error, 
                            // service offline, etc
                            console.log(this.message + error);

                        });

                }
            },
            created: function() {
                this.getAllOrders();
            }
        });
    </script>



    <?php include "footer.html" ?>



</body>

</html>