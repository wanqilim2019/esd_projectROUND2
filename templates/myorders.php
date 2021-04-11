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
                <div class="container">
                    {% if data[0].required_info|length > 0 %}
                    <ul class="list-group">

                        {% for d in data[0].required_info %}
                        <li class="list-group-item">
                            <div class="row">
                                <img class="col-3" src="{{ url_for('static', filename='images/') }}{{ d.imgname }}"
                                    style="border-top-left-radius: 20px;border-top-right-radius: 20px">
                                <div class="col-3">
                                    <h2>{{ d.pname }}</h2>
                                    {% if session['acctType'] == 'business' %}
                                    <h5>{{ d.address }}</h5>
                                    {% endif %}
                                    <h5 id='statusline'>{{ d.dStatus }}</h5>
                                </div>
                                <div class="col-2"></div>
                                <div class="col-3">
                                    <h5>{{ d.datetime }}</h5>
                                    <h2>Quantity: {{ d.quantity }}</h2>
                                    <!-- button to fulfill order -->
                                    {% if session['acctType'] == 'business' and d.dStatus == 'Unfulfilled' %}
                                    <input type="hidden" id="oid" name="oid" value="{{d.oid}}" />
                                    <input type="hidden" id="dstatus" name="dstatus" value="{{d.dStatus}}" />
                                    <button id='submit' class="btn btn-warning">Fulfil Order</button>
                                    {% endif %}
                                </div>
                            </div>
                        </li>
                        {% endfor %}
                    </ul>
                    {% else %}
                    <div>
                        <h1>No Orders!</h1>
                        <h2>You have not order anything.</h2>
                        <p><a href="{{url_for('.home')}}"> Shop here now</a></p>
                    </div>
                    {% endif %}

                </div>

            </div>
        </div>
        <script type="text/javascript">
            $(document).ready(function () {
                $('#submit').click(function () {
                    console.log("click");
                    var oid = String($('#oid').val());
                    console.log(oid);
                    var dstatus = $('#dstatus').val();
                    if (dstatus == 'Unfulfilled') {
                        $.ajax({
                            url: 'http://localhost:5400/fulfill_order',    //Your api url
                            type: 'PUT',   //type is any HTTP method
                            data: {
                                data: {
                                    'oid': oid,
                                    'dStatus': 'Fulfilled'
                            }
                            },      //Data as js object
                            success: function () {
                                $('#statusline').innerText = 'Fulfilled';
                            }
                        })
                            ;
                    }


                });
            });

        </script>


    </div>

    <?php include "footer.html" ?>



</body>

</html>