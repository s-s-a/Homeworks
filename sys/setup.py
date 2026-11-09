from setuptools import setup, find_packages

setup(
    name="sys_homework",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        # Зависимости для проекта (если есть)
        # pytest для запуска тестов
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Домашние задания по модулю sys в Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sys_homework",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)