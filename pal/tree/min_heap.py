#!/usr/bin/env python
#coding: utf8

import heapq

class MinHeap:
  def __init__(self):
    self._data = []

  def size(self):
    return len(self._data) - 1

  def top(self):
    assert self.size() > 0
    return self._data[0]

  def push(self, value):
    heapq.heappush(self._data, value)

  def pop(self):
    '''min heap'''
    assert self.size() > 0
    return heapq.heappop(self._data)
