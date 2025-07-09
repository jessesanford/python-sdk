"""Test for proxy_oauth package."""


def test_package_import():
    """Test that the package can be imported."""
    import proxy_oauth
    
    assert proxy_oauth.__version__ == "0.1.0"


def test_package_structure():
    """Test that the package has the expected structure."""
    import proxy_oauth
    
    # Verify the package is properly structured
    assert hasattr(proxy_oauth, "__version__")
    assert isinstance(proxy_oauth.__version__, str)