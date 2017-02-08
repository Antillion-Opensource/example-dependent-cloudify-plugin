# Dependent Cloudify Plugin

This plugin demonstrates an approach to using the code (and, indirectly,
types) of another Cloudify plugin within another plugin.

The challenge is that Cloudify deploys each plugin individually,
so when the plugin runs remotely, it does not bring along any dependencies.

## Solution: embed + requirements + blueprint embedded

Constraint: this plugin must be embedded into the blueprint; it cannot
(yet) be used online or managed.

It forms 3 parts: the embedded plugin, the requirements file and the
plugin declaration

## The embedded plugin

The plugin this depends on (example-cloudify-plugin) is git subtree'd
into the `dependencies` directory, so that the code is entirely
present.

## The requirements file & the plugin declaration

Cloudify allows plugins to specify extra `install_arguments` that are
supplied to pip during plugin install time.

The requirements file looks like this:

        dependencies/example-cloudify-plugin/

The plugin declaration looks like so:

        plugins:
          dependent:
            executor: central_deployment_agent
            source: dependent-cloudify-plugin
            install_arguments: -r embedded-requirements.txt

# Dependent types

This plugin's type `antillion.demo.DependentNode` derives from the
other plugin`s type `antillion.demo.DummyNode`, however this plugin
 makes no reference to the other plugin's type file.

 To use this plugin, the blueprint must explicitly include the other
 plugin's type file. When Cloudify brings the entire blueprint together,
 the hierarchy will be valid.

# Usage

With both plugins embedded into a blueprint, a working example looks
like this:

        tosca_definitions_version: cloudify_dsl_1_3

        imports:
          - http://www.getcloudify.org/spec/cloudify/3.4.1/types.yaml
          - plugins/example-cloudify-plugin/embedded.plugin.yml
          - plugins/example-cloudify-plugin/types/dummy.types.yml
          - plugins/example-dependent-cloudify-plugin/depends-embedded.plugin.yml
          - plugins/example-dependent-cloudify-plugin/types/depends.types.yml

        node_templates:
          dummy1:
            type: antillion.demo.DummyNode


          dependent1:
            type: antillion.demo.DependentNode

# Final notes

It's important to note that this plugin's `setup.py` does not declare
the dependent plugin in `install_requires`.
