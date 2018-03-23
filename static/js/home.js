var tableData = [];

$(document).ready(function () {
  $('.deadline').hide();
  var table = $('#table').dataTable({
    data: tableData,
    aoColumnDefs: [
      {
        bSortable: false,
        aTargets: [2, 3, 4, 6]
      }
    ],
    searching: false,
    columns: [
      {data: 'id'},
      {data: 'sponsor'},
      {data: 'title'},
      {
        data: 'link',
        render: function (data, type, row) {
          return `<a href="${data}">${data}</a>`;
        }
      },
      {data: 'amount'},
      {data: 'deadline'},
      {
        data: 'synopsis',
        render: function (data, type, row) {
          return '<button class="btn btn-primary" onclick="swal(\'Synopisis\',\`' + `${data}\`);">View</button>`;
        }
      }
    ]
  });

  $('#searchType').on('change', function () {
    if (this.value === 'sponsor') {
      $('#search').show();
      $('.deadline').hide();
    } else {
      $('#search').hide();
      $('.deadline').show();
    }
  });

  var form = $('#search-form');
  form.ajaxForm({
    delegation: true,
    success: function (data, statusText, xhr, $form) {
      table.fnClearTable();
      if (data.length > 0) {
       table.fnAddData(data);
      }
    }
  });
  form.submit();

});
