var tableData = [];

const numberWithCommas = (x) => {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};

$(document).ready(function () {
  $('#search').hide();
  $('.deadline').hide();
  $('#anything').hide();
  var table = $('#table').dataTable({
    data: tableData,
    columns: [
      {data: 'id'},
      {data: 'sponsor'},{
        data: 'title',
        render: function (data, type, row) {
          return `<span>${data} <a onclick="swal('Synopisis',\`${row.synopsis}\n${row.awards}\`);">Synopsis >></a></span>`;
        }
      },{
        data: 'link',
        render: function (data, type, row) {
          return `<a href="${data}" target="_blank">${data}</a>`;
        }
      },{
        data: 'amount',
        render: function (data, type, row) {
          if (data === 'undisclosed')
            return data;
          return data ? '$' + numberWithCommas(data) : '';

        }
      },{
        data: 'deadline',
        render: function (data, type, row) {

          return data ? moment(data).format('DD/MM/YYYY') : '';
        }
      },
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
  $('table').excelTableFilter();
});
