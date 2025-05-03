from setuptools import setup, find_packages

setup(
    name="QuantWork",
    version="0.1.0",
    description="A financial data and quant modeling library.",
    author="Anthony Dopke",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "yfinance",
        "pandas",
        "numpy",
        "matplotlib",
        "scipy",
    ],
    python_requires=">=3.8",
)
