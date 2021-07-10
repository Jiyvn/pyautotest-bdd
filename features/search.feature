Feature: 百度搜索
    需求描述: 百度搜索http://www.baidu.com

Scenario: 搜索pytest
    Given 搜索词:pytest
    And 浏览器:safari
    When 打开百度，输入搜索词搜索
    And 打开

Scenario: 搜索2pytest
    Given 搜索词:pytest
    When 打开百度，输入搜索词搜索