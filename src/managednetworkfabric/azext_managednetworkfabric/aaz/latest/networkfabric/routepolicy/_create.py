# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "networkfabric routepolicy create",
)
class Create(AAZCommand):
    """Create a Route Policy resource

    :example: Create a Route Policy Example 1
        az networkfabric routepolicy create --resource-group "example-rg" --resource-name "example-routepolicy" --location "westus3" --default-action "Permit" --nf-id "/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/networkFabrics/example-fabric" --address-family-type "IPv4" --statements "[{sequenceNumber:1234,condition:{ipCommunityIds:['/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/ipCommunities/example-ipCommunityName'],ipPrefixId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/ipPrefixes/example-ipPrefixName',type:Or},action:{localPreference:123,actionType:Permit,ipCommunityProperties:{add:{ipCommunityIds:['/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/ipCommunities/example-ipCommunityName']}}}}]"

    :example: Create a Route Policy Example 2
        az networkfabric routepolicy create --resource-group "example-rg" --resource-name "example-routepolicy" --location "westus3" --default-action "Permit" --nf-id "/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/networkFabrics/example-fabric" --address-family-type "IPv4" --statements "[{sequenceNumber:1235,condition:{ipExtendedCommunityIds:['/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/ipExtendedCommunities/example-ipExtendedCommunityName'],type:And},action:{localPreference:1235,actionType:Deny,ipExtendedCommunityProperties:{set:{ipExtendedCommunityIds:['/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/ipExtendedCommunities/example-ipExtendedCommunityName']}}}}]"

    :example: Help text for sub parameters under the specific parent can be viewed by using the shorthand syntax '??'. See https://github.com/Azure/azure-cli/tree/dev/doc/shorthand_syntax.md for more about shorthand syntax.
        az networkfabric routepolicy create --statements "??"
        az networkfabric routepolicy create --statements "[{action:??"
        az networkfabric routepolicy create --statements "[{action:{ip-community-properties:??"
    """

    _aaz_info = {
        "version": "2023-06-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/routepolicies/{}", "2023-06-15"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group",
            required=True,
        )
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Name of the Route Policy.",
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Body",
            help="Location of Azure region",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Body",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.address_family_type = AAZStrArg(
            options=["--address-family-type"],
            arg_group="Properties",
            help="AddressFamilyType. This parameter decides whether the given ipv4 or ipv6 route policy. Default value is IPv4.",
            enum={"IPv4": "IPv4", "IPv6": "IPv6"},
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        _args_schema.annotation = AAZStrArg(
            options=["--annotation"],
            arg_group="Properties",
            help="Description for underlying resource.",
        )
        _args_schema.default_action = AAZStrArg(
            options=["--default-action"],
            arg_group="Properties",
            help="Default action that needs to be applied when no condition is matched. Example: Permit.",
            enum={"Deny": "Deny", "Permit": "Permit"},
        )
        _args_schema.nf_id = AAZResourceIdArg(
            options=["--nf-id"],
            arg_group="Properties",
            help="ARM Resource ID of the Network Fabric.",
            required=True,
        )
        _args_schema.statements = AAZListArg(
            options=["--statements"],
            arg_group="Properties",
            help="Route Policy statements.",
            required=True,
        )

        statements = cls._args_schema.statements
        statements.Element = AAZObjectArg()

        _element = cls._args_schema.statements.Element
        _element.action = AAZObjectArg(
            options=["action"],
            help="Route policy action properties.",
            required=True,
        )
        _element.annotation = AAZStrArg(
            options=["annotation"],
            help="Description for underlying resource.",
        )
        _element.condition = AAZObjectArg(
            options=["condition"],
            help="Route policy condition properties.",
            required=True,
        )
        _element.sequence_number = AAZIntArg(
            options=["sequence-number"],
            help="Sequence to insert to/delete from existing route.",
            required=True,
            fmt=AAZIntArgFormat(
                maximum=4294967295,
                minimum=1,
            ),
        )

        action = cls._args_schema.statements.Element.action
        action.action_type = AAZStrArg(
            options=["action-type"],
            help="Action type. Example: Permit.",
            required=True,
            enum={"Continue": "Continue", "Deny": "Deny", "Permit": "Permit"},
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        action.ip_community_properties = AAZObjectArg(
            options=["ip-community-properties"],
            help="IP Community Properties.",
        )
        action.ip_extended_community_properties = AAZObjectArg(
            options=["ip-extended-community-properties"],
            help="IP Extended Community Properties.",
        )
        action.local_preference = AAZIntArg(
            options=["local-preference"],
            help="Local Preference of the route policy.",
            fmt=AAZIntArgFormat(
                maximum=4294967295,
                minimum=0,
            ),
        )

        ip_community_properties = cls._args_schema.statements.Element.action.ip_community_properties
        ip_community_properties.add = AAZObjectArg(
            options=["add"],
            help="List of IP Community IDs.",
        )
        cls._build_args_ip_community_id_list_create(ip_community_properties.add)
        ip_community_properties.delete = AAZObjectArg(
            options=["delete"],
            help="List of IP Community IDs.",
        )
        cls._build_args_ip_community_id_list_create(ip_community_properties.delete)
        ip_community_properties.set = AAZObjectArg(
            options=["set"],
            help="List of IP Community IDs.",
        )
        cls._build_args_ip_community_id_list_create(ip_community_properties.set)

        ip_extended_community_properties = cls._args_schema.statements.Element.action.ip_extended_community_properties
        ip_extended_community_properties.add = AAZObjectArg(
            options=["add"],
            help="List of IP Extended Community IDs.",
        )
        cls._build_args_ip_extended_community_id_list_create(ip_extended_community_properties.add)
        ip_extended_community_properties.delete = AAZObjectArg(
            options=["delete"],
            help="List of IP Extended Community IDs.",
        )
        cls._build_args_ip_extended_community_id_list_create(ip_extended_community_properties.delete)
        ip_extended_community_properties.set = AAZObjectArg(
            options=["set"],
            help="List of IP Extended Community IDs.",
        )
        cls._build_args_ip_extended_community_id_list_create(ip_extended_community_properties.set)

        condition = cls._args_schema.statements.Element.condition
        condition.ip_community_ids = AAZListArg(
            options=["ip-community-ids"],
            help="List of IP Community resource IDs.",
        )
        condition.ip_extended_community_ids = AAZListArg(
            options=["ip-extended-community-ids"],
            help="List of IP Extended Community resource IDs.",
        )
        condition.ip_prefix_id = AAZStrArg(
            options=["ip-prefix-id"],
            help="Arm Resource Id of IpPrefix.",
        )
        condition.type = AAZStrArg(
            options=["type"],
            help="Type of the condition used. Default value is Or.",
            enum={"And": "And", "Or": "Or"},
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        ip_community_ids = cls._args_schema.statements.Element.condition.ip_community_ids
        ip_community_ids.Element = AAZStrArg()

        ip_extended_community_ids = cls._args_schema.statements.Element.condition.ip_extended_community_ids
        ip_extended_community_ids.Element = AAZStrArg()
        return cls._args_schema

    _args_ip_community_id_list_create = None

    @classmethod
    def _build_args_ip_community_id_list_create(cls, _schema):
        if cls._args_ip_community_id_list_create is not None:
            _schema.ip_community_ids = cls._args_ip_community_id_list_create.ip_community_ids
            return

        cls._args_ip_community_id_list_create = AAZObjectArg()

        ip_community_id_list_create = cls._args_ip_community_id_list_create
        ip_community_id_list_create.ip_community_ids = AAZListArg(
            options=["ip-community-ids"],
            help="List of IP Community resource IDs.",
        )

        ip_community_ids = cls._args_ip_community_id_list_create.ip_community_ids
        ip_community_ids.Element = AAZStrArg()

        _schema.ip_community_ids = cls._args_ip_community_id_list_create.ip_community_ids

    _args_ip_extended_community_id_list_create = None

    @classmethod
    def _build_args_ip_extended_community_id_list_create(cls, _schema):
        if cls._args_ip_extended_community_id_list_create is not None:
            _schema.ip_extended_community_ids = cls._args_ip_extended_community_id_list_create.ip_extended_community_ids
            return

        cls._args_ip_extended_community_id_list_create = AAZObjectArg()

        ip_extended_community_id_list_create = cls._args_ip_extended_community_id_list_create
        ip_extended_community_id_list_create.ip_extended_community_ids = AAZListArg(
            options=["ip-extended-community-ids"],
            help="List of IP Extended Community resource IDs.",
        )

        ip_extended_community_ids = cls._args_ip_extended_community_id_list_create.ip_extended_community_ids
        ip_extended_community_ids.Element = AAZStrArg()

        _schema.ip_extended_community_ids = cls._args_ip_extended_community_id_list_create.ip_extended_community_ids

    def _execute_operations(self):
        self.pre_operations()
        yield self.RoutePoliciesCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class RoutePoliciesCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/routePolicies/{routePolicyName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "routePolicyName", self.ctx.args.resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-06-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("addressFamilyType", AAZStrType, ".address_family_type")
                properties.set_prop("annotation", AAZStrType, ".annotation")
                properties.set_prop("defaultAction", AAZStrType, ".default_action")
                properties.set_prop("networkFabricId", AAZStrType, ".nf_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("statements", AAZListType, ".statements", typ_kwargs={"flags": {"required": True}})

            statements = _builder.get(".properties.statements")
            if statements is not None:
                statements.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.statements[]")
            if _elements is not None:
                _elements.set_prop("action", AAZObjectType, ".action", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("annotation", AAZStrType, ".annotation")
                _elements.set_prop("condition", AAZObjectType, ".condition", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("sequenceNumber", AAZIntType, ".sequence_number", typ_kwargs={"flags": {"required": True}})

            action = _builder.get(".properties.statements[].action")
            if action is not None:
                action.set_prop("actionType", AAZStrType, ".action_type", typ_kwargs={"flags": {"required": True}})
                action.set_prop("ipCommunityProperties", AAZObjectType, ".ip_community_properties")
                action.set_prop("ipExtendedCommunityProperties", AAZObjectType, ".ip_extended_community_properties")
                action.set_prop("localPreference", AAZIntType, ".local_preference")

            ip_community_properties = _builder.get(".properties.statements[].action.ipCommunityProperties")
            if ip_community_properties is not None:
                _CreateHelper._build_schema_ip_community_id_list_create(ip_community_properties.set_prop("add", AAZObjectType, ".add"))
                _CreateHelper._build_schema_ip_community_id_list_create(ip_community_properties.set_prop("delete", AAZObjectType, ".delete"))
                _CreateHelper._build_schema_ip_community_id_list_create(ip_community_properties.set_prop("set", AAZObjectType, ".set"))

            ip_extended_community_properties = _builder.get(".properties.statements[].action.ipExtendedCommunityProperties")
            if ip_extended_community_properties is not None:
                _CreateHelper._build_schema_ip_extended_community_id_list_create(ip_extended_community_properties.set_prop("add", AAZObjectType, ".add"))
                _CreateHelper._build_schema_ip_extended_community_id_list_create(ip_extended_community_properties.set_prop("delete", AAZObjectType, ".delete"))
                _CreateHelper._build_schema_ip_extended_community_id_list_create(ip_extended_community_properties.set_prop("set", AAZObjectType, ".set"))

            condition = _builder.get(".properties.statements[].condition")
            if condition is not None:
                condition.set_prop("ipCommunityIds", AAZListType, ".ip_community_ids")
                condition.set_prop("ipExtendedCommunityIds", AAZListType, ".ip_extended_community_ids")
                condition.set_prop("ipPrefixId", AAZStrType, ".ip_prefix_id")
                condition.set_prop("type", AAZStrType, ".type")

            ip_community_ids = _builder.get(".properties.statements[].condition.ipCommunityIds")
            if ip_community_ids is not None:
                ip_community_ids.set_elements(AAZStrType, ".")

            ip_extended_community_ids = _builder.get(".properties.statements[].condition.ipExtendedCommunityIds")
            if ip_extended_community_ids is not None:
                ip_extended_community_ids.set_elements(AAZStrType, ".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.address_family_type = AAZStrType(
                serialized_name="addressFamilyType",
            )
            properties.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            properties.annotation = AAZStrType()
            properties.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            properties.default_action = AAZStrType(
                serialized_name="defaultAction",
            )
            properties.network_fabric_id = AAZStrType(
                serialized_name="networkFabricId",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.statements = AAZListType(
                flags={"required": True},
            )

            statements = cls._schema_on_200_201.properties.statements
            statements.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.statements.Element
            _element.action = AAZObjectType(
                flags={"required": True},
            )
            _element.annotation = AAZStrType()
            _element.condition = AAZObjectType(
                flags={"required": True},
            )
            _element.sequence_number = AAZIntType(
                serialized_name="sequenceNumber",
                flags={"required": True},
            )

            action = cls._schema_on_200_201.properties.statements.Element.action
            action.action_type = AAZStrType(
                serialized_name="actionType",
                flags={"required": True},
            )
            action.ip_community_properties = AAZObjectType(
                serialized_name="ipCommunityProperties",
            )
            action.ip_extended_community_properties = AAZObjectType(
                serialized_name="ipExtendedCommunityProperties",
            )
            action.local_preference = AAZIntType(
                serialized_name="localPreference",
            )

            ip_community_properties = cls._schema_on_200_201.properties.statements.Element.action.ip_community_properties
            ip_community_properties.add = AAZObjectType()
            _CreateHelper._build_schema_ip_community_id_list_read(ip_community_properties.add)
            ip_community_properties.delete = AAZObjectType()
            _CreateHelper._build_schema_ip_community_id_list_read(ip_community_properties.delete)
            ip_community_properties.set = AAZObjectType()
            _CreateHelper._build_schema_ip_community_id_list_read(ip_community_properties.set)

            ip_extended_community_properties = cls._schema_on_200_201.properties.statements.Element.action.ip_extended_community_properties
            ip_extended_community_properties.add = AAZObjectType()
            _CreateHelper._build_schema_ip_extended_community_id_list_read(ip_extended_community_properties.add)
            ip_extended_community_properties.delete = AAZObjectType()
            _CreateHelper._build_schema_ip_extended_community_id_list_read(ip_extended_community_properties.delete)
            ip_extended_community_properties.set = AAZObjectType()
            _CreateHelper._build_schema_ip_extended_community_id_list_read(ip_extended_community_properties.set)

            condition = cls._schema_on_200_201.properties.statements.Element.condition
            condition.ip_community_ids = AAZListType(
                serialized_name="ipCommunityIds",
            )
            condition.ip_extended_community_ids = AAZListType(
                serialized_name="ipExtendedCommunityIds",
            )
            condition.ip_prefix_id = AAZStrType(
                serialized_name="ipPrefixId",
            )
            condition.type = AAZStrType()

            ip_community_ids = cls._schema_on_200_201.properties.statements.Element.condition.ip_community_ids
            ip_community_ids.Element = AAZStrType()

            ip_extended_community_ids = cls._schema_on_200_201.properties.statements.Element.condition.ip_extended_community_ids
            ip_extended_community_ids.Element = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    @classmethod
    def _build_schema_ip_community_id_list_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("ipCommunityIds", AAZListType, ".ip_community_ids")

        ip_community_ids = _builder.get(".ipCommunityIds")
        if ip_community_ids is not None:
            ip_community_ids.set_elements(AAZStrType, ".")

    @classmethod
    def _build_schema_ip_extended_community_id_list_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("ipExtendedCommunityIds", AAZListType, ".ip_extended_community_ids")

        ip_extended_community_ids = _builder.get(".ipExtendedCommunityIds")
        if ip_extended_community_ids is not None:
            ip_extended_community_ids.set_elements(AAZStrType, ".")

    _schema_ip_community_id_list_read = None

    @classmethod
    def _build_schema_ip_community_id_list_read(cls, _schema):
        if cls._schema_ip_community_id_list_read is not None:
            _schema.ip_community_ids = cls._schema_ip_community_id_list_read.ip_community_ids
            return

        cls._schema_ip_community_id_list_read = _schema_ip_community_id_list_read = AAZObjectType()

        ip_community_id_list_read = _schema_ip_community_id_list_read
        ip_community_id_list_read.ip_community_ids = AAZListType(
            serialized_name="ipCommunityIds",
        )

        ip_community_ids = _schema_ip_community_id_list_read.ip_community_ids
        ip_community_ids.Element = AAZStrType()

        _schema.ip_community_ids = cls._schema_ip_community_id_list_read.ip_community_ids

    _schema_ip_extended_community_id_list_read = None

    @classmethod
    def _build_schema_ip_extended_community_id_list_read(cls, _schema):
        if cls._schema_ip_extended_community_id_list_read is not None:
            _schema.ip_extended_community_ids = cls._schema_ip_extended_community_id_list_read.ip_extended_community_ids
            return

        cls._schema_ip_extended_community_id_list_read = _schema_ip_extended_community_id_list_read = AAZObjectType()

        ip_extended_community_id_list_read = _schema_ip_extended_community_id_list_read
        ip_extended_community_id_list_read.ip_extended_community_ids = AAZListType(
            serialized_name="ipExtendedCommunityIds",
        )

        ip_extended_community_ids = _schema_ip_extended_community_id_list_read.ip_extended_community_ids
        ip_extended_community_ids.Element = AAZStrType()

        _schema.ip_extended_community_ids = cls._schema_ip_extended_community_id_list_read.ip_extended_community_ids


__all__ = ["Create"]
