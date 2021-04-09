<!doctype html>
<html lang="en">

<head>
  <?php include "head.html" ?>


  <style>
    .box {
      width: 400px;
      height: auto;
    }

    .form-group {
      width: 400px;
    }

    .center {
      margin-left: 350px;
    }
  </style>
  <title>Product Listing</title>
</head>

<body>

<?php include "nav.html" ?>


  <div class="container mx-auto text-center justify-content-center">
    <h1>Add a new product</h1>



    <form class="justify-content-center" method="POST" action="http://localhost:5001/product">
    <?php if( $_GET['pid']) {?>
    <div class="alert alert-success" role="alert">
        Product Created! PID: <?php echo $_GET['pid'] ?>
      </div>      
      <?php } ?>
      <div class="row justify-content-center">

        <div class="form-group">
          <label for="=PName">Product Name:</label>
          <input type="text" class="form-control" name='pname' id="Pname" placeholder=" Product Name">
        </div>
      </div>

      <div class="row justify-content-center">
        <div class="form-group">
          <label for="exampleInputFile">Insert Image</label>
          <small id="fileHelp" class="form-text text-muted">Please upload an image of your product.</small>
          <input type='file' name="imgfile" onchange="readImg(this);" />
          <img id="pic" src="#" alt="" aria-describedby="fileHelp" />


          <script>
            function readImg(input) {
              if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                  $('#pic')
                    .attr('src', e.target.result)
                    .width(300)
                    .height(300);
                };

                reader.readAsDataURL(input.files[0]);
              }
            }
          </script>

        </div>
      </div>

      <div class="row justify-content-center">
        <label for="Price">Product Price: </label>

        <span class="input-group-text col-1" id="addon-wrapping" style="margin-left:10px">S$</span>
        <input type="text" class="col-3" placeholder="0.00" aria-label="Product Price" name="price"
          aria-describedby="addon-wrapping">
      </div>

      <div class="row justify-content-center">
        <div class="form-group">
          <label for="Description">Product Description:</label>
          <textarea class="form-control" id="Description" name="pdesc"
            placeholder="Write a short description about your product..." rows="3"></textarea>
        </div>
        <input type="hidden" name="bid" value="{{session['data']['bid']}}">

      </div>
      </br>
      <div class="row justify-content-center">
        <button type="submit" class="btn btn-warning col-2">Add Product</button>

      </div>
    </form>

  </div>
  <?php include "footer.html" ?>


</body>

</html>