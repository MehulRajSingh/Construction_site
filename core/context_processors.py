def project_context(request):
    """
    Context processor that makes data available to all templates
    """
    context = {
        # Add any global context variables you need here
        'site_name': 'Construction Site',
        'company_name': 'Your Company Name',
        # Add other global variables as needed
    }
    return context