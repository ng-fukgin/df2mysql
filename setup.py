from setuptools import setup

setup(
    name='df2mysql',
    version='0.0.1',
    author='wfj',
    author_email='wfj.0000@gmail.com',
    description='提供了一组方法，用于与 Microsoft SQL Server 数据库进行交互。允许执行各种操作，如连接到 SQL Server、创建和删除数据库、创建和删除表、添加和删除列、插入和检索数据等。',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ng-fukgin/df2mysql',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    keywords='df2mysql, Microsoft SQL Server, 数据库交互, 数据库连接, 数据库操作, 数据库管理',
    python_requires='>=3.7',
    install_requires=[
        'pymssql',
        'pandas',
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/ng-fukgin/df2mysql/issues',
        'Documentation': 'https://github.com/ng-fukgin/df2mysql/wiki',
        'Source Code': 'https://github.com/ng-fukgin/df2mysql',
    },
    license='MIT',
    platforms='any',
    include_package_data=True,
    zip_safe=False,
)
