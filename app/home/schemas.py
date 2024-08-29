"""Schemas for Home App."""

from pydantic import BaseModel


class Faqs(BaseModel):

    id: int
    question: str
    answer: str


class Project(BaseModel):

    id: int
    image: str
    title: str
    category: str


class Service(BaseModel):

    id: int
    title: str
    image: str
    description: str
    link: str


class StrategyCard(BaseModel):

    id: int
    title: str
    description: str


class Team(BaseModel):

    id: int
    image: str
    name: str
    area: str
    slogan: str


class Testimonial(BaseModel):

    id: int
    author: str
    image: str
    area: str
    testimonial: str
