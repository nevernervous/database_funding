$(document).ready(function () {
    $('#table').dataTable({
        aoColumnDefs: [
            {
                bSortable: false,
                aTargets: [2, 3, 4, 6]
            }
        ],
        searching: false
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
});