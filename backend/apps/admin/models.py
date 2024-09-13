#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  #
#  Copyright (C) 2023 ZinoHome, Inc. All Rights Reserved
#  #
#  @Time    : 2023
#  @Author  : Zhang Jun
#  @Email   : ibmzhangjun@139.com
#  @Software: SwiftApp

from typing import Optional
from sqlmodel import SQLModel
from fastapi_amis_admin import amis
from fastapi_amis_admin.models import Field


# Create your models here.

# class Category(SQLModel, table=True):
#     __tablename__ = 'blog_category'
#     id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
#     name: str = Field(
#         title='Category Name',
#         unique=True,
#         index=True,
#         nullable=False,
#     )
#     description: str = Field(default='', title='Description', amis_form_item=amis.Textarea())
#     is_active: bool = Field(False, title='Is Active')
