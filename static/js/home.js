var tableData = [];

$(document).ready(function () {
  $('.deadline').hide();
  $('#anything').hide();
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
    const search = $('#search').hide();
    const deadline = $('.deadline').hide();
    const anything = $('#anything').hide();
    switch (this.value) {
      case 'sponsor':
        search.show();
        break;
      case 'deadline':
        deadline.show();
        break;
      case 'anything':
        anything.show();
        break;
    }
  });

  var form = $('#search-form');
  form.ajaxForm({
    delegation: true,
    error: function (data, statusText, xhr, $form) {
      table.fnClearTable();
    },
    success: function (data, statusText, xhr, $form) {
      table.fnClearTable();
      if (data.length > 0) {
       table.fnAddData(data);
      }
    }
  });
  form.submit();

});
