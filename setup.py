"""
Setup script for pip installation of the cell‑analysis pipelines.
"""

from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent

# Optional: read long description from README.md if it exists
readme_path = this_directory / "README.md"
long_description = readme_path.read_text() if readme_path.exists() else ""

setup(
    name="cell-analysis-pipelines",
    version="0.1.0",
    description="Python port of MATLAB cell‑analysis pipelines (GFAP, Hoechst, NeuN, SOX9)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="MohammadrezaRH",
    author_email="mrahmanimanesh@uvic.ca",
    license="MIT",
    py_modules=["gfap", "hoechst", "neun", "sox9", "run_sample_images"],
    install_requires=[
        "numpy>=1.18.0",
        "pandas>=1.0.0",
        "scikit-image>=0.17.0",
    ],
    entry_points={
        "console_scripts": [
            "gfap=gfap:_main",
            "hoechst=hoechst:_main",
            "neun=neun:_main",
            "sox9=sox9:_main",
            "run-sample-images=run_sample_images:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
