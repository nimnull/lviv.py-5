#!/usr/bin/env python
import click

@click.group()
def main():
  pass


@main.command()
def client():
  pass


@main.command()
def server():
  pass

if __name__ == '__main__':
  main()
